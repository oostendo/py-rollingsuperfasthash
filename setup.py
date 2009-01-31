from distutils.core import setup, Extension

setup(name = "rollingsuperfasthash",
      version = "0.1",
      ext_modules = [Extension("rollingsuperfasthash", ["rollingsuperfasthash.c"])])

