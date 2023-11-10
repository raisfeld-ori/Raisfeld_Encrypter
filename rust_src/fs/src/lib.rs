use pyo3::prelude::*;
use pyo3::types::PyBytes;

extern crate tokio;
extern crate pyo3_asyncio;
use crate::tokio::io::AsyncWriteExt;

// import a python module, can't be used async
#[pyfunction]
fn get_dir() -> PyResult<String>{
    return Python::with_gil(|py| {
        let appdirs = py.import("appdirs")?;
        let appdirs = appdirs.getattr("AppDirs")?;
        let appdirs = appdirs.call1(("hidden", "hidden"))?;
        let appdirs =  appdirs.getattr("user_data_dir")?;

        return Ok(appdirs.to_string());
    });
}
#[pyfunction]
pub fn create_dir(py: Python, dir: &str) -> PyResult<()>{
    let dir = get_dir()? + "\\" + dir;
    return pyo3_asyncio::tokio::run(py, async move{ tokio::fs::create_dir_all(dir).await?; Ok(())});
}

#[pyfunction]
pub fn write_file(py: Python, file: &str, text: &PyBytes)->PyResult<()>{
    let text = text.as_bytes().to_vec();
    let file = get_dir()? + "\\" + file;
    return pyo3_asyncio::tokio::run(py, async move {
        let mut file = tokio::fs::File::create(file).await?;
        file.write(&text).await?;
        return Ok(());
    });
}

#[pyfunction]
pub fn read_file(py: Python, file: &str) -> PyResult<PyObject>{
    let file = get_dir()? + "\\" + file;

    let data = pyo3_asyncio::tokio::run(py, async move {
        return Ok(tokio::fs::read(file).await);
    });
    return Ok(PyBytes::new(py, &data??).into());
}


#[pymodule]
fn fs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(write_file))?;
    m.add_wrapped(wrap_pyfunction!(create_dir))?;
    m.add_wrapped(wrap_pyfunction!(read_file))?;
    Ok(())
}

#[tokio::test]
async fn test_function(){
    pyo3::prepare_freethreaded_python();
    
}

