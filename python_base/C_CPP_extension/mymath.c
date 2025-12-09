#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <omp.h>

// 一个并行计算数组平方和的函数
static PyObject* parallel_sum(PyObject* self, PyObject* args) {
    PyObject* listObj;
    if (!PyArg_ParseTuple(args, "O", &listObj)) {
        return NULL;
    }

    if (!PyList_Check(listObj)) {
        PyErr_SetString(PyExc_TypeError, "参数必须是一个list");
        return NULL;
    }

    long n = PyList_Size(listObj);
    double sum = 0.0;

    #pragma omp parallel for reduction(+:sum)
    for (long i = 0; i < n; i++) {
        PyObject* item = PyList_GetItem(listObj, i);  // 借用引用，不需要 Py_DECREF
        double val = PyFloat_AsDouble(item);
        sum += val * val;  // 计算平方和
    }

    return Py_BuildValue("d", sum);
}

// 方法定义表
static PyMethodDef MyMethods[] = {
    {"parallel_sum", parallel_sum, METH_VARARGS, "计算列表中所有元素平方和（并行版）"},
    {NULL, NULL, 0, NULL}
};

// 模块定义
static struct PyModuleDef mymathmodule = {
    PyModuleDef_HEAD_INIT,
    "mymath",
    NULL,
    -1,
    MyMethods
};

// 模块初始化
PyMODINIT_FUNC PyInit_mymath(void) {
    return PyModule_Create(&mymathmodule);
}
