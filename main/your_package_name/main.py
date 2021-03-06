import importhook
import ic

modules = [
    "__future__",
    "array",
    "html",
    "runpy",
    "_abc",
    "ast",
    "html5lib",
    "sched",
    "_ast",
    "asttokens",
    "http",
    "search",
    "_asyncio",
    "asynchat",
    "icecream",
    "searchAgents",
    "_bisect",
    "asyncio",
    "idlelib",
    "searchTestClasses",
    "_blake2",
    "asyncore",
    "idna",
    "secrets",
    "_bootlocale",
    "atexit",
    "imaplib",
    "select",
    "_bz2",
    "audioop",
    "imghdr",
    "selectors",
    "_codecs",
    "autograder",
    "imp",
    "setuptools",
    "_codecs_cn",
    "base64",
    "importhook",
    "shelve",
    "_codecs_hk",
    "bdb",
    "importlib",
    "shlex",
    "_codecs_iso2022",
    "binascii",
    "inspect",
    "shutil",
    "_codecs_jp",
    "binhex",
    "io",
    "signal",
    "_codecs_kr",
    "bisect",
    "ipaddress",
    "site",
    "_codecs_tw",
    "builtins",
    "itertools",
    "sitecustomize",
    "_collections",
    "bz2",
    "json",
    "six",
    "_collections_abc",
    "cProfile",
    "keyboardAgents",
    "smtpd",
    "_compat_pickle",
    "cachecontrol",
    "keyring",
    "smtplib",
    "_compression",
    "cachy",
    "keyword",
    "sndhdr",
    "_contextvars",
    "calendar",
    "layout",
    "socket",
    "_crypt",
    "certifi",
    "lib2to3",
    "socketserver",
    "_csv",
    "cgi",
    "libfuturize",
    "sqlite3",
    "_ctypes",
    "cgitb",
    "libpasteurize",
    "sre_compile",
    "_ctypes_test",
    "chardet",
    "linecache",
    "sre_constants",
    "_curses",
    "chunk",
    "locale",
    "sre_parse",
    "_curses_panel",
    "cleo",
    "lockfile",
    "ssl",
    "_datetime",
    "clikit",
    "logging",
    "stat",
    "_dbm",
    "cmath",
    "lzma",
    "statistics",
    "_decimal",
    "cmd",
    "mailbox",
    "string",
    "_dummy_thread",
    "code",
    "mailcap",
    "stringprep",
    "_elementtree",
    "codecs",
    "marshal",
    "struct",
    "_functools",
    "codeop",
    "math",
    "submission_autograder",
    "_gdbm",
    "collections",
    "mimetypes",
    "subprocess",
    "_hashlib",
    "colorama",
    "mmap",
    "sunau",
    "_heapq",
    "colorsys",
    "modulefinder",
    "super_map",
    "_imp",
    "compileall",
    "msgpack",
    "symbol",
    "_io",
    "concurrent",
    "multiAgents",
    "symtable",
    "_json",
    "configparser",
    "multiagentTestClasses sys",
    "_locale",
    "contextlib",
    "multiprocessing",
    "sysconfig",
    "_lsprof",
    "contextvars",
    "netrc",
    "syslog",
    "_lzma",
    "copy",
    "nntplib",
    "tabnanny",
    "_markupbase",
    "copyreg",
    "ntpath",
    "tarfile",
    "_md5",
    "crashtest",
    "nturl2path",
    "telnetlib",
    "_multibytecodec",
    "crypt",
    "numbers",
    "tempfile",
    "_multiprocessing",
    "csv",
    "opcode",
    "termios",
    "_opcode",
    "ctypes",
    "operator",
    "test",
    "_operator",
    "curses",
    "optparse",
    "testClasses",
    "_osx_support",
    "dataclasses",
    "os",
    "testParser",
    "_pickle",
    "datetime",
    "packaging",
    "textDisplay",
    "_posixshmem",
    "dbm",
    "pacman",
    "textwrap",
    "_posixsubprocess",
    "debug",
    "pacmanAgents",
    "this",
    "_py_abc",
    "decimal",
    "parser",
    "threading",
    "_pydecimal",
    "difflib",
    "past",
    "time",
    "_pyio",
    "dis",
    "pastel",
    "timeit",
    "_queue",
    "distlib",
    "pathlib",
    "tkinter",
    "_random",
    "distutils",
    "pbr",
    "token",
    "_scproxy",
    "doctest",
    "pdb",
    "tokenize",
    "_sha1",
    "dummy_threading",
    "pexpect",
    "trace",
    "_sha256",
    "easy_install",
    "pickle",
    "traceback",
    "_sha3",
    "eightpuzzle",
    "pickletools",
    "tracemalloc",
    "_sha512",
    "email",
    "pip",
    "tty",
    "_signal",
    "encodings",
    "pipes",
    "turtle",
    "_sitebuiltins",
    "ensurepip",
    "pkg_resources",
    "turtledemo",
    "_socket",
    "enum",
    "pkgutil",
    "types",
    "_sqlite3",
    "errno",
    "platform",
    "typing",
    "_sre",
    "executing",
    "plistlib",
    "unicodedata",
    "_ssl",
    "faulthandler",
    "poetry",
    "unittest",
    "_stat",
    "fcntl",
    "poplib",
    "urllib",
    "_statistics",
    "filecmp",
    "posix",
    "urllib3",
    "_string",
    "fileinput",
    "posixpath",
    "util",
    "_strptime",
    "filelock",
    "pprint",
    "uu",
    "_struct",
    "fnmatch",
    "profile",
    "uuid",
    "_symtable",
    "formatter",
    "projectParams",
    "venv",
    "_sysconfigdata__darwin_darwin fractions",
    "pstats",
    "virtualenv",
    "_testbuffer",
    "ftplib",
    "pty",
    "warnings",
    "_testcapi",
    "functools",
    "pwd",
    "wave",
    "_testimportmultiple future",
    "py_compile",
    "weakref",
    "_testinternalcapi",
    "game",
    "pyclbr",
    "webbrowser",
    "_testmultiphase",
    "gc",
    "pydoc",
    "webencodings",
    "_thread",
    "genericpath",
    "pydoc_data",
    "wheel",
    "_threading_local",
    "getopt",
    "pyexpat",
    "wsgiref",
    "_tkinter",
    "getpass",
    "pygments",
    "xdrlib",
    "_tracemalloc",
    "gettext",
    "pylev",
    "xml",
    "_warnings",
    "ghostAgents",
    "pyparsing",
    "xmlrpc",
    "_weakref",
    "glob",
    "queue",
    "xxlimited",
    "_weakrefset",
    "grading",
    "quopri",
    "xxsubtype",
    "_xxsubinterpreters",
    "graphicsDisplay",
    "random",
    "zipapp",
    "_xxtestfuzz",
    "graphicsUtils",
    "re",
    "zipfile",
    "abc",
    "grp",
    "readline",
    "zipimport",
    "aifc",
    "gzip",
    "reprlib",
    "zlib",
    "antigravity",
    "hashlib",
    "requests",
    "appdirs",
    "heapq",
    "resource",
    "argparse",
    "hmac",
    "rlcompleter",
]
# ^ from python -c "help()" <<< "modules" 
for each in modules:
    @importhook.on_import(each)
    def _(a_module):
        print(f'{a_module} has been imported')
        for each_key in dir(a_module):
            if callable(each_key):
                # FIXME, wrap / replace it 


raise Exception('Implement your functions here')