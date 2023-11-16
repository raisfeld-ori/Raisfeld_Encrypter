use pyo3::prelude::*;
use pyo3::types::PyBytes;

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

#[pyfunction]
pub fn read_dir(py: Python, dir: String) -> PyResult<Vec<String>>{
    return pyo3_asyncio::tokio::run(py, async move{
        let mut files = tokio::fs::read_dir(dir).await?;
        let mut result: Vec<String> = Vec::new();
        while let Ok(Some(file)) = files.next_entry().await{
            result.push(file.file_name().to_str().unwrap().to_string());
        }
        
        Ok(result)
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
        println!("{:?}", read_dir(py, String::from("./")));
    });
}

