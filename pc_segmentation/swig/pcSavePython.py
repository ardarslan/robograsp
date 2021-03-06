# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pcSavePython', [dirname(__file__)])
        except ImportError:
            import _pcSavePython
            return _pcSavePython
        if fp is not None:
            try:
                _mod = imp.load_module('_pcSavePython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pcSavePython = swig_import_helper()
    del swig_import_helper
else:
    import _pcSavePython
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class floatArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, floatArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, floatArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pcSavePython.new_floatArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pcSavePython.delete_floatArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _pcSavePython.floatArray___getitem__(self, *args)
    def __setitem__(self, *args): return _pcSavePython.floatArray___setitem__(self, *args)
    def cast(self): return _pcSavePython.floatArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _pcSavePython.floatArray_frompointer
    if _newclass:frompointer = staticmethod(_pcSavePython.floatArray_frompointer)
floatArray_swigregister = _pcSavePython.floatArray_swigregister
floatArray_swigregister(floatArray)

def floatArray_frompointer(*args):
  return _pcSavePython.floatArray_frompointer(*args)
floatArray_frompointer = _pcSavePython.floatArray_frompointer


def save(*args):
  return _pcSavePython.save(*args)
save = _pcSavePython.save

def fini():
  return _pcSavePython.fini()
fini = _pcSavePython.fini

def isSaving():
  return _pcSavePython.isSaving()
isSaving = _pcSavePython.isSaving

def getFileFeatures(*args):
  return _pcSavePython.getFileFeatures(*args)
getFileFeatures = _pcSavePython.getFileFeatures

def getNumberOfFeatures():
  return _pcSavePython.getNumberOfFeatures()
getNumberOfFeatures = _pcSavePython.getNumberOfFeatures
# This file is compatible with both classic and new-style classes.


def init(_use_ros = True, ros_topic = "/asus/depth_registered/points", 
    sleep_milisec = 10):
  return _pcSavePython.init(_use_ros, ros_topic, sleep_milisec)
init = _pcSavePython.init

def initFeats(_argv = None):
  return _pcSavePython.initFeats(_argv)
initFeats = _pcSavePython.initFeats

def getCurrentFeatures(*args):
  return _pcSavePython.getCurrentFeatures(*args)
getCurrentFeatures = _pcSavePython.getCurrentFeatures

