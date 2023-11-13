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
pub fn read_file(py: Python, file: String) -> PyResult<PyObject>{
    let file = file;

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
