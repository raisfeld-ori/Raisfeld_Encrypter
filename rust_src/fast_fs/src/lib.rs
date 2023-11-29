use std::path::PathBuf;
use std::fs::remove_file;

use pyo3::prelude::*;
use pyo3::types::PyBytes;
use tokio::fs::DirEntry;
use tokio::sync::mpsc;

extern crate tokio;
extern crate pyo3_asyncio;
use crate::tokio::io::AsyncWriteExt;



#[pyfunction]
pub fn create_dir(py: Python, dir: String) -> PyResult<()>{
    return pyo3_asyncio::tokio::run(py, async move{ tokio::fs::create_dir_all(dir).await?; Ok(())});
}

#[pyfunction]
pub fn write_file(py: Python, file: String, text: &PyBytes)->PyResult<()>{
    let text = text.as_bytes().to_vec();
    return pyo3_asyncio::tokio::run(py, async move {
        let mut file = tokio::fs::File::create(file).await?;
        file.write(&text).await?;
        return Ok(());
    });
}


#[derive(Debug)]
#[pyclass]
pub struct DirFile{
    pub file: DirEntry,
    pub path: PathBuf,
    pub file_name: String,

}

impl DirFile{
    async fn new(file: DirEntry) -> Self {
        return Self{
            file_name: file.file_name().to_str().unwrap().to_string(),
            path: file.path(),
            file,
        }
    }
}

#[pymethods]
impl DirFile{
    pub fn name(&self)->Option<String>{Some(self.path.file_stem()?.to_str()?.to_string())}
    pub fn extension(&self)->Option<String>{Some(self.file.path().extension()?.to_str()?.to_string())}
    pub fn read(&self, py: Python)->Option<Py<PyAny>>{
        let file = read_file(py, self.path.to_str()?.to_string());
        if file.is_err() {return None;}
        else{return Some(file.unwrap());}
    }
    pub fn delete(&self) -> PyResult<()>{Ok(remove_file(self.file.path())?)}
}

#[pyfunction]
pub fn read_dir(py: Python, dir: String) -> PyResult<Vec<DirFile>>{
    return pyo3_asyncio::tokio::run(py, async move{
        let mut files = tokio::fs::read_dir(dir).await?;
        let (snd,mut rcv) = mpsc::unbounded_channel();
        while let Ok(Some(file)) = files.next_entry().await{
            let _ = snd.send(DirFile::new(file));
        }
        let mut result = Vec::new();
        while let Ok(file) = rcv.try_recv(){
            result.push(file.await);
        }
        return Ok(result);
    });
}

#[pyfunction]
pub fn read_file(py: Python, file: String) -> PyResult<PyObject>{
    let file = file;

    let data = pyo3_asyncio::tokio::run(py, async move {
        return Ok(tokio::fs::read(file).await);
    });
    return Ok(PyBytes::new(py, &data??).into());
}

#[pymodule]
fn fast_fs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(write_file))?;
    m.add_wrapped(wrap_pyfunction!(create_dir))?;
    m.add_wrapped(wrap_pyfunction!(read_file))?;
    m.add_wrapped(wrap_pyfunction!(read_dir))?;
    Ok(())
}

#[test]
pub fn test_fn(){
    pyo3::prepare_freethreaded_python();
    pyo3::Python::with_gil(|py|{
        let files = read_dir(py, String::from("./")).unwrap();
        let file = files.iter().nth(2).unwrap();
        println!("{:?}", file.delete());
    });
}

