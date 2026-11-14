---
title: "satyr-python-2(3)"
name: "satyr-python-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-satyr-python-2/"
description: "satyr-python – satyr python API"
---

<p>satyr-python &#8211; satyr python API </p>
<p> Contents:</p>
<h2>Report</h2>
<p>A <code>Report</code> object represents a single problem report in the <i>uReport format</i>.</p>
<dl>
<dt><code>class satyr.Report</code></p>
<dd>satyr.Report &#8211; report containing all data relevant to a software problem </p>
<p> Usage: </p>
<p> satyr.Report() &#8211; creates an empty report object </p>
<p> satyr.Report(json_string) &#8211; creates a report from its JSON representation</p>
<dt><code>auth</code></p>
<dd>Dictinary of key/value pairs used for authentication</p>
<dt><code>component_name</code></p>
<dd>Name of the software component this report pertains to (string)</p>
<dt><code>operating_system</code></p>
<dd>Operating system (<code>OperatingSystem</code> object)</p>
<dt><code>packages</code></p>
<dd>List of packages (currently a list of <code>RpmPackage</code> objects)</p>
<dt><code>report_type</code></p>
<dd>Report type (string)</p>
<dt><code>report_version</code></p>
<dd>Version of the report (int)</p>
<dt><code>reporter_name</code></p>
<dd>Name of the reporting software (string)</p>
<dt><code>reporter_version</code></p>
<dd>Version of the reporting software (string)</p>
<dt><code>stacktrace</code></p>
<dd>Problem stacktrace (<code>SingleThreadStacktrace</code> or <code>MultiThreadStacktrace</code> object)</p>
<dt><code>to_json()</code></p>
<dd>Usage: report.to_json() </p>
<p> Returns: string &#8211; the report serialized as JSON</p>
<dt><code>user_local</code></p>
<dd>Did the problem originate in a program executed by local user? (bool)</p>
<dt><code>user_root</code></p>
<dd>Did the problem originate in a program running as root? (bool)</dl>
<h3>Operating system</h3>
<p>Data about operating system are stored in the <code>OperatingSystem</code> object.</p>
<dl>
<dt><code>class satyr.OperatingSystem</code></p>
<dd>satyr.OperatingSystem &#8211; describes an operating system </p>
<p> Usage: </p>
<p> satyr.OperatingSystem() &#8211; creates an empty operating system object </p>
<p> satyr.OperatingSystem(name, version, arch) &#8211; creates an operating system object with given properties (all arguments are strings or None)</p>
<dt><code>architecture</code></p>
<dd>Architecture (string)</p>
<dt><code>cpe</code></p>
<dd>Common platform enumeration identifier (string)</p>
<dt><code>name</code></p>
<dd>Operating system name (string)</p>
<dt><code>uptime</code></p>
<dd>Machine uptime (long)</p>
<dt><code>version</code></p>
<dd>Version (string)</dl>
<h3>Package</h3>
<p>The <code>Report</code> can contain a list of software packages. Currently, only <i>RPM</i> packages are supported.</p>
<dl>
<dt><code>class satyr.RpmPackage</code></p>
<dd>satyr.RpmPackage &#8211; RPM package representation </p>
<p> Usage: </p>
<p> satyr.RpmPackage() &#8211; creates an empty RPM package object </p>
<p> satyr.RpmPackage(name, epoch, version, release, arch) &#8211; creates RPM package object with given properties</p>
<dt><code>architecture</code></p>
<dd>Architecture (string)</p>
<dt><code>epoch</code></p>
<dd>Epoch (int)</p>
<dt><code>install_time</code></p>
<dd>Time of installation (long)</p>
<dt><code>name</code></p>
<dd>Package name (string)</p>
<dt><code>release</code></p>
<dd>Release (string)</p>
<dt><code>role</code></p>
<dd>Role the package plays in the problem. Currently ROLE_UNKNOWN or ROLE_AFFECTED.</p>
<dt><code>version</code></p>
<dd>Version (string)</dl>
<h2>Stacktrace</h2>
<p>Each problem has its own frame, stacktrace and thread type (for problems that can have multiple threads). </p>
<p> <code>WARNING:</code> The <code>GdbFrame</code>, <code>GdbThread</code>, and <code>GdbStacktrace</code> have rather limited functionality, cannot be used in reports, and will probably be removed in the future.</p>
<h3>Frame classes</h3>
<p>Stack frame corresponds to a function invocation saved on the stack. All frame types are derived from the <code>BaseFrame</code>.</p>
<h3>BaseFrame</h3>
<dl>
<dt><code>class satyr.BaseFrame</code></p>
<dd>satyr.BaseFrame &#8211; base class for call frames</p>
<dt><code>equals()</code></p>
<dd>Usage: frame.equals(otherframe) </p>
<p> Returns: bool &#8211; True if frame has attributes equal to otherframe</p>
<dt><code>short_string()</code></p>
<dd>Usage: frame.short_string() </p>
<p> Returns: string &#8211; brief textual representation of the frame</dl>
<h3>CoreFrame</h3>
<dl>
<dt><code>class satyr.CoreFrame</code></p>
<dd>satyr.CoreFrame &#8211; class representing a frame in a native executable </p>
<p> Usage: satyr.CoreFrame() &#8211; creates an empty frame</p>
<dt><code>address</code></p>
<dd>Address of the machine code in memory (long)</p>
<dt><code>build_id</code></p>
<dd>Build ID of the ELF file (string)</p>
<dt><code>build_id_offset</code></p>
<dd>Offset of the instruction pointer from the start of the executable segment (long)</p>
<dt><code>dup()</code></p>
<dd>Usage: frame.dup() </p>
<p> Returns: satyr.CoreFrame &#8211; a new clone of the frame </p>
<p> Clones the frame object. All new structures are independent of the original object.</p>
<dt><code>file_name</code></p>
<dd>Name of the executable or shared library (string)</p>
<dt><code>fingerprint</code></p>
<dd>Fingerprint of the current function (string)</p>
<dt><code>fingerprint_hashed</code></p>
<dd>True if fingerprint is already hashed (bool)</p>
<dt><code>function_name</code></p>
<dd>Function name (string)</dl>
<h3>JavaFrame</h3>
<dl>
<dt><code>class satyr.JavaFrame</code></p>
<dd>satyr.JavaFrame &#8211; class representing a java frame </p>
<p> Usage: </p>
<p> satyr.JavaFrame() &#8211; creates an empty frame </p>
<p> satyr.JavaFrame(str) &#8211; parses str and fills the frame object</p>
<dt><code>class_path</code></p>
<dd>Class path (string)</p>
<dt><code>dup()</code></p>
<dd>Usage: frame.dup() </p>
<p> Returns: satyr.JavaFrame &#8211; a new clone of frame </p>
<p> Clones the frame object. All new structures are independent of the original object.</p>
<dt><code>file_line</code></p>
<dd>File line (positive integer)</p>
<dt><code>file_name</code></p>
<dd>File name (string)</p>
<dt><code>is_exception</code></p>
<dd>True if frame is an exception frame (bool)</p>
<dt><code>is_native</code></p>
<dd>True if method is native, always false if frame is an exception (bool)</p>
<dt><code>message</code></p>
<dd>Exception message (string)</p>
<dt><code>name</code></p>
<dd>Fully qualified domain name (string)</dl>
<h3>KerneloopsFrame</h3>
<dl>
<dt><code>class satyr.KerneloopsFrame</code></p>
<dd>satyr.KerneloopsFrame &#8211; class representing a frame in a kerneloops </p>
<p> Usage: </p>
<p> satyr.KerneloopsFrame() &#8211; creates an empty frame </p>
<p> satyr.KerneloopsFrame(str) &#8211; parses str and fills the frame object</p>
<dt><code>address</code></p>
<dd>Address of the current instruction (long)</p>
<dt><code>dup()</code></p>
<dd>Usage: frame.dup() </p>
<p> Returns: satyr.KerneloopsFrame &#8211; a new clone of frame </p>
<p> Clones the frame object. All new structures are independent of the original object.</p>
<dt><code>from_address</code></p>
<dd>Address of the caller&#8217;s instruction (long)</p>
<dt><code>from_function_length</code></p>
<dd>Caller function length (long)</p>
<dt><code>from_function_name</code></p>
<dd>Caller function name (string)</p>
<dt><code>from_function_offset</code></p>
<dd>Caller function offset (long)</p>
<dt><code>from_module_name</code></p>
<dd>Module owning the caller function (string)</p>
<dt><code>function_length</code></p>
<dd>Function length (long)</p>
<dt><code>function_name</code></p>
<dd>Function name (string)</p>
<dt><code>function_offset</code></p>
<dd>Function offset (long)</p>
<dt><code>module_name</code></p>
<dd>Module owning the function (string)</p>
<dt><code>reliable</code></p>
<dd>True if the the frame is guaranteed to be real (bool)</p>
<dt><code>special_stack</code></p>
<dd>Identifier of x86_64 kernel stack (string)</dl>
<h3>PythonFrame</h3>
<dl>
<dt><code>class satyr.PythonFrame</code></p>
<dd>satyr.PythonFrame &#8211; class representing a python frame </p>
<p> Usage: </p>
<p> satyr.PythonFrame() &#8211; creates an empty frame </p>
<p> satyr.PythonFrame(str) &#8211; parses str and fills the frame object</p>
<dt><code>dup()</code></p>
<dd>Usage: frame.dup() </p>
<p> Returns: satyr.PythonFrame &#8211; a new clone of frame </p>
<p> Clones the frame object. All new structures are independent of the original object.</p>
<dt><code>file_line</code></p>
<dd>Source line number (positive integer)</p>
<dt><code>file_name</code></p>
<dd>Source file name (string)</p>
<dt><code>function_name</code></p>
<dd>Function name (string)</p>
<dt><code>line_contents</code></p>
<dd>Remaining line contents (string)</p>
<dt><code>special_file</code></p>
<dd>True if the frame is not a real file, like stdin or eval&#8217;d string (bool)</p>
<dt><code>special_function</code></p>
<dd>True if the frame doesn&#8217;t belong to a named function, e.g. lambda or a module</dl>
<h3>GdbFrame</h3>
<dl>
<dt><code>class satyr.GdbFrame</code></p>
<dd>satyr.GdbFrame &#8211; class representing a frame in a thread </p>
<p> Usage: </p>
<p> satyr.GdbFrame() &#8211; creates an empty frame </p>
<p> satyr.GdbFrame(str) &#8211; parses str and fills the frame object</p>
<dt><code>address</code></p>
<dd>Address of the current instruction (long)</p>
<dt><code>calls_func()</code></p>
<dd>Usage: frame.calls_func(name) </p>
<p> name: string &#8211; function name </p>
<p> Returns: integer &#8211; 0 = False, 1 = True </p>
<p> Checks whether the frame represents a call to a function with given name.</p>
<dt><code>calls_func_in_file()</code></p>
<dd>Usage: frame.calls_func_in_file(name, filename) </p>
<p> name: string &#8211; function name </p>
<p> filename: string &#8211; file name </p>
<p> Returns: integer &#8211; 0 = False, 1 = True </p>
<p> Checks whether the frame represents a call to a function with given name from a given file.</p>
<dt><code>dup()</code></p>
<dd>Usage: frame.dup() </p>
<p> Returns: satyr.GdbFrame &#8211; a new clone of the frame </p>
<p> Clones the frame object. All new structures are independent of the original object.</p>
<dt><code>function_name</code></p>
<dd>Function name (string)</p>
<dt><code>function_type</code></p>
<dd>Function type (string)</p>
<dt><code>library_name</code></p>
<dd>Executable file name (string)</p>
<dt><code>number</code></p>
<dd>Frame number (positive integer)</p>
<dt><code>signal_handler_called</code></p>
<dd>True if the frame is signal handler (bool)</p>
<dt><code>source_file</code></p>
<dd>Source file name (string)</p>
<dt><code>source_line</code></p>
<dd>Source line number (positive integer)</dl>
<h3>Thread classes</h3>
<p>Thread classes are defined only for problems that can have multiple thread. They all have <code>BaseThread</code> as a base class.</p>
<h3>BaseThread</h3>
<dl>
<dt><code>class satyr.BaseThread</code></p>
<dd>satyr.BaseThread &#8211; base class for threads</p>
<dt><code>distance()</code></p>
<dd>Usage: thread.distance(other, dist_type=DISTANCE_LEVENSHTEIN) </p>
<p> other: other thread </p>
<p> dist_type (optional): one of DISTANCE_LEVENSHTEIN, DISTANCE_JARO_WINKLER, DISTANCE_JACCARD or DISTANCE_DAMERAU_LEVENSHTEIN </p>
<p> Returns: positive float &#8211; distance between the two threads</p>
<dt><code>equals()</code></p>
<dd>Usage: frame.equals(otherthread) </p>
<p> Returns: bool &#8211; True if thread has attributes equal to otherthread</p>
<dt><code>frames</code></p>
<dd>A list containing objects representing frames in a thread.</p>
<dt><code>get_duphash()</code></p>
<dd>Usage: thread.get_duphash(frames=0, flags=DUPHASH_NORMAL, prefix=&#8221;) </p>
<p> Returns: string &#8211; thread&#8217;s duplication hash </p>
<p> frames: integer &#8211; number of frames to use (default 0 means use all) </p>
<p> flags: integer &#8211; bitwise sum of flags (DUPHASH_NORMAL, DUPHASH_NOHASH, DUPHASH_NONORMALIZE, DUPHASH_KOOPS_COMPAT) </p>
<p> prefix: string &#8211; string to be prepended in front of the text before hashing</dl>
<h3>CoreThread</h3>
<dl>
<dt><code>class satyr.CoreThread</code></p>
<dd>satyr.CoreThread &#8211; class representing a thread in a stacktrace </p>
<p> Usage: satyr.CoreThread() &#8211; creates an empty thread</p>
<dt><code>dup()</code></p>
<dd>Usage: thread.dup() </p>
<p> Returns: satyr.CoreThread &#8211; a new clone of thread </p>
<p> Clones the thread object. All new structures are independent of the original object.</dl>
<h3>JavaThread</h3>
<dl>
<dt><code>class satyr.JavaThread</code></p>
<dd>satyr.JavaThread &#8211; class representing a thread in a stacktrace </p>
<p> Usage: </p>
<p> satyr.JavaThread() &#8211; creates an empty thread </p>
<p> satyr.JavaThread(str) &#8211; parses str and fills the thread object</p>
<dt><code>dup()</code></p>
<dd>Usage: thread.dup() </p>
<p> Returns: satyr.JavaThread &#8211; a new clone of thread </p>
<p> Clones the thread object. All new structures are independent of the original object.</p>
<dt><code>format_funs()</code></p>
<dd>Usage: thread.format_funs() </p>
<p> Returns: string</p>
<dt><code>name</code></p>
<dd>Thread name (string)</p>
<dt><code>quality()</code></p>
<dd>Usage: thread.quality() </p>
<p> Returns: float &#8211; 0..1, thread quality </p>
<p> Computes the ratio #good / #all. See quality_counts method for more.</p>
<dt><code>quality_counts()</code></p>
<dd>Usage: thread.quality_counts() </p>
<p> Returns: tuple (ok, all) &#8211; ok representing number of &#8216;good&#8217; frames, all representing total number of frames </p>
<p> Counts the number of &#8216;good&#8217; frames and the number of all frames. &#8216;Good&#8217; means the function name is known (not just &#8216;??&#8217;).</dl>
<h3>GdbThread</h3>
<dl>
<dt><code>class satyr.GdbThread</code></p>
<dd>satyr.GdbThread &#8211; class representing a thread in a stacktrace </p>
<p> Usage: </p>
<p> satyr.GdbThread() &#8211; creates an empty thread </p>
<p> satyr.GdbThread(str) &#8211; parses str and fills the thread object </p>
<p> satyr.GdbThread(str, only_funs=True) &#8211; parses list of function names</p>
<dt><code>dup()</code></p>
<dd>Usage: thread.dup() </p>
<p> Returns: satyr.GdbThread &#8211; a new clone of thread </p>
<p> Clones the thread object. All new structures are independent of the original object.</p>
<dt><code>format_funs()</code></p>
<dd>Usage: thread.format_funs() </p>
<p> Returns: string</p>
<dt><code>number</code></p>
<dd>Thread number (positive integer)</p>
<dt><code>quality()</code></p>
<dd>Usage: thread.quality() </p>
<p> Returns: float &#8211; 0..1, thread quality </p>
<p> Computes the ratio #good / #all. See quality_counts method for more.</p>
<dt><code>quality_counts()</code></p>
<dd>Usage: thread.quality_counts() </p>
<p> Returns: tuple (ok, all) &#8211; ok representing number of &#8216;good&#8217; frames, all representing total number of frames </p>
<p> Counts the number of &#8216;good&#8217; frames and the number of all frames. &#8216;Good&#8217; means the function name is known (not just &#8216;??&#8217;).</dl>
<h3>Stacktrace classes</h3>
<p>Single threaded stacktraces have <code>SingleThreadStacktrace</code> as their base class, which is in turn derived from <code>BaseThread</code>. This means that <code>SingleThreadStacktrace</code> can be treated as a thread:</p>
<dl>
<dt>&bull;</p>
<dd><code>Kerneloops</code></p>
<dt>&bull;</p>
<dd><code>PythonStacktrace</code> </p>
<p> Stacktrace types with the possibility of multiple threads are derived from <code>MultiThreadStacktrace</code>:</p>
<dt>&bull;</p>
<dd><code>CoreStacktrace</code></p>
<dt>&bull;</p>
<dd><code>JavaStacktrace</code></p>
<dt>&bull;</p>
<dd><code>GdbStacktrace</code></dl>
<h3>SingleThreadStacktrace</h3>
<dl>
<dt><code>class satyr.SingleThreadStacktrace</code></p>
<dd>satyr.SingleThreadStacktrace &#8211; base class for stacktrace with single thread</p>
<dt><code>crash_thread</code></p>
<dd>Reference to the thread that caused the crash, if known</p>
<dt><code>static from_json()</code></p>
<dd>Usage: SomeStacktrace.from_json(json_string) (class method) </p>
<p> Returns: stacktrace (of SomeStacktrace class) deserialized from json_string </p>
<p> json_string: string &#8211; json input</p>
<dt><code>get_bthash()</code></p>
<dd>Usage: stacktrace.get_bthash([flags]) </p>
<p> Returns: string &#8211; hash of the stacktrace </p>
<p> flags: integer &#8211; bitwise sum of flags (BTHASH_NORMAL, BTHASH_NOHASH)</p>
<dt><code>to_short_text()</code></p>
<dd>Usage: stacktrace.to_short_text([max_frames]) </p>
<p> Returns short text representation of the stacktrace. If max_frames is specified, the result includes only that much topmost frames.</dl>
<h3>MultiThreadStacktrace</h3>
<dl>
<dt><code>class satyr.MultiThreadStacktrace</code></p>
<dd>satyr.MultiThreadStacktrace &#8211; base class for stacktrace with multiple threads</p>
<dt><code>crash_thread</code></p>
<dd>Reference to the thread that caused the crash, if known</p>
<dt><code>static from_json()</code></p>
<dd>Usage: SomeStacktrace.from_json(json_string) (class method) </p>
<p> Returns: stacktrace (of SomeStacktrace class) deserialized from json_string </p>
<p> json_string: string &#8211; json input</p>
<dt><code>get_bthash()</code></p>
<dd>Usage: stacktrace.get_bthash([flags]) </p>
<p> Returns: string &#8211; hash of the stacktrace </p>
<p> flags: integer &#8211; bitwise sum of flags (BTHASH_NORMAL, BTHASH_NOHASH)</p>
<dt><code>threads</code></p>
<dd>A list containing the objects representing threads in the stacktrace.</p>
<dt><code>to_short_text()</code></p>
<dd>Usage: stacktrace.to_short_text([max_frames]) </p>
<p> Returns short text representation of the stacktrace. If max_frames is specified, the result includes only that much topmost frames.</dl>
<h3>CoreStacktrace</h3>
<dl>
<dt><code>class satyr.CoreStacktrace</code></p>
<dd>satyr.CoreStacktrace &#8211; class representing a core stacktrace </p>
<p> Usage: </p>
<p> satyr.CoreStacktrace() &#8211; creates an empty stacktrace </p>
<p> satyr.CoreStacktrace(json) &#8211; creates stacktrace object from JSON string</p>
<dt><code>dup()</code></p>
<dd>Usage: stacktrace.dup() </p>
<p> Returns: satyr.CoreStacktrace &#8211; a new clone of core stacktrace </p>
<p> Clones the stacktrace object. All new structures are independent of the original object.</p>
<dt><code>executable</code></p>
<dd>Name of the executable (string)</p>
<dt><code>signal</code></p>
<dd>Signal number (int)</dl>
<h3>JavaStacktrace</h3>
<dl>
<dt><code>class satyr.JavaStacktrace</code></p>
<dd>satyr.JavaStacktrace &#8211; class representing a java stacktrace </p>
<p> Usage: </p>
<p> satyr.JavaStacktrace() &#8211; creates an empty stacktrace </p>
<p> satyr.JavaStacktrace(str) &#8211; parses str and fills the stacktrace object</p>
<dt><code>dup()</code></p>
<dd>Usage: stacktrace.dup() </p>
<p> Returns: satyr.JavaStacktrace &#8211; a new clone of java stacktrace </p>
<p> Clones the stacktrace object. All new structures are independent of the original object.</dl>
<h3>Kerneloops</h3>
<dl>
<dt><code>class satyr.Kerneloops</code></p>
<dd>satyr.Kerneloops &#8211; class representing a kerneloops stacktrace </p>
<p> Usage: </p>
<p> satyr.Kerneloops() &#8211; creates an empty kerneloops stacktrace </p>
<p> satyr.Kerneloops(str) &#8211; parses str and fills the kerneloops stacktrace object</p>
<dt><code>dup()</code></p>
<dd>Usage: stacktrace.dup() </p>
<p> Returns: satyr.Kerneloops &#8211; a new clone of kerneloops stacktrace </p>
<p> Clones the kerneloops object. All new structures are independent of the original object.</p>
<dt><code>modules</code></p>
<dd>Modules loaded at the time of the event (list of strings)</p>
<dt><code>normalize()</code></p>
<dd>Usage: stacktrace.normalize() </p>
<p> Normalizes the stacktrace.</p>
<dt><code>raw_oops</code></p>
<dd>Original text of the kerneloops (string)</p>
<dt><code>taint_flags</code></p>
<dd>Dictionary of kernel taint flags. Keys are the flag names, values are booleans indicating whether the flag is set.</p>
<dt><code>version</code></p>
<dd>Kernel version (string)</dl>
<h3>PythonStacktrace</h3>
<dl>
<dt><code>class satyr.PythonStacktrace</code></p>
<dd>satyr.PythonStacktrace &#8211; class representing a python stacktrace </p>
<p> Usage: </p>
<p> satyr.PythonStacktrace() &#8211; creates an empty python stacktrace </p>
<p> satyr.PythonStacktrace(str) &#8211; parses str and fills the python stacktrace object</p>
<dt><code>dup()</code></p>
<dd>Usage: stacktrace.dup() </p>
<p> Returns: satyr.PythonStacktrace &#8211; a new clone of python stacktrace </p>
<p> Clones the PythonStacktrace object. All new structures are independent of the original object.</p>
<dt><code>exception_name</code></p>
<dd>Exception type (string)</dl>
<h3>GdbStacktrace</h3>
<dl>
<dt><code>class satyr.GdbStacktrace</code></p>
<dd>satyr.GdbStacktrace &#8211; class representing a stacktrace </p>
<p> Usage: </p>
<p> satyr.GdbStacktrace() &#8211; creates an empty stacktrace </p>
<p> satyr.GdbStacktrace(str) &#8211; parses str and fills the stacktrace object</p>
<dt><code>crashframe</code></p>
<dd>Readonly. By default the field contains None. After calling the find_crash_frame method, a reference to satyr.Frame object is stored into the field.</p>
<dt><code>dup()</code></p>
<dd>Usage: stacktrace.dup() </p>
<p> Returns: satyr.GdbStacktrace &#8211; a new clone of stacktrace </p>
<p> Clones the stacktrace object. All new structures are independent of the original object.</p>
<dt><code>find_address()</code></p>
<dd>Usage: stacktrace.find_address(address) </p>
<p> address: long &#8211; address to find </p>
<p> Returns: satyr.Sharedlib object or None if not found </p>
<p> Looks whether the given address belongs to a shared library.</p>
<dt><code>find_crash_frame()</code></p>
<dd>Usage: stacktrace.find_crash_frame() </p>
<p> Returns: satyr.Frame &#8211; crash frame </p>
<p> Finds crash frame in the stacktrace. Also sets the stacktrace.crashframe field.</p>
<dt><code>libs</code></p>
<dd>A list containing the satyr.Sharedlib objects representing shared libraries loaded at the moment of crash.</p>
<dt><code>limit_frame_depth()</code></p>
<dd>Usage: stacktrace.limit_frame_depth(N) </p>
<p> N: positive integer &#8211; frame depth </p>
<p> Crops all threads to only contain first N frames.</p>
<dt><code>normalize()</code></p>
<dd>Usage: stacktrace.normalize() </p>
<p> Normalizes all threads in the stacktrace.</p>
<dt><code>quality_complex()</code></p>
<dd>Usage: stacktrace.quality_complex() </p>
<p> Returns: float &#8211; 0..1, stacktrace quality </p>
<p> Computes the quality from stacktrace, crash thread and frames around the crash.</p>
<dt><code>quality_simple()</code></p>
<dd>Usage: stacktrace.quality_simple() </p>
<p> Returns: float &#8211; 0..1, stacktrace quality </p>
<p> Computes the quality from stacktrace itself.</p>
<dt><code>set_libnames()</code></p>
<dd>Usage: stacktrace.set_libnames() </p>
<p> Sets library names according to sharedlibs data.</p>
<dt><code>to_short_text()</code></p>
<dd>Usage: stacktrace.to_short_text([max_frames]) </p>
<p> Returns short text representation of the crash thread. If max_frames is specified, the result includes only that much topmost frames.</dl>
<h2>Clustering</h2>
<h3>Distance matrix</h3>
<dl>
<dt><code>class satyr.Distances</code></p>
<dd>satyr.Distances &#8211; class representing distances between objects </p>
<p> Usage: </p>
<p> satyr.Distances(m, n) &#8211; creates an m-by-n distance matrix </p>
<p> satyr.Distances([threads], m, dist_type=DISTANCE_LEVENSHTEIN) &#8211; compares first m threads with others </p>
<p> dist_type (optional): DISTANCE_LEVENSHTEIN, DISTANCE_JACCARD or DISTANCE_DAMERAU_LEVENSHTEIN</p>
<dt><code>dup()</code></p>
<dd>Usage: distances.dup() </p>
<p> Returns: satyr.Distances &#8211; a new clone of the distances </p>
<p> Clones the distances object. All new structures are independent of the original object.</p>
<dt><code>get_distance()</code></p>
<dd>Usage: distances.get_distance(i, j) </p>
<p> Returns: positive float &#8211; distance between objects i and j</p>
<dt><code>get_size()</code></p>
<dd>Usage: distances.get_size() </p>
<p> Returns: (m, n) &#8211; size of the distance matrix</p>
<dt><code>set_distance()</code></p>
<dd>Usage: distances.set_distance(i, j, d) </p>
<p> Sets distance between objects i and j to d</dl>
<h3>Dendrogram</h3>
<dl>
<dt><code>class satyr.Dendrogram</code></p>
<dd>satyr.Dendrogram &#8211; a dendrogram created by clustering algorithm </p>
<p> Usage: satyr.Dendrogram(distances) &#8211; creates new dendrogram from a distance matrix</p>
<dt><code>cut()</code></p>
<dd>Usage: dendrogram.cut(level, min_size) </p>
<p> Returns: list of clusters (lists of objects) which have at least min_size objects and which were merged at most at the specified distance</p>
<dt><code>get_merge_level()</code></p>
<dd>Usage: dendrogram.get_merge_level(i) </p>
<p> Returns: float &#8211; merge level between clusters at positions i and i + 1</p>
<dt><code>get_object()</code></p>
<dd>Usage: dendrogram.get_object(i) </p>
<p> Returns: integer &#8211; index of the object at position i</p>
<dt><code>get_size()</code></p>
<dd>Usage: dendrogram.get_size() </p>
<p> Returns: integer &#8211; number of objects in the dendrogram</p>
<dt>&bull;</p>
<dd><i>genindex</i></p>
<dt>&bull;</p>
<dd><i>modindex</i></p>
<dt>&bull;</p>
<dd><i>search</i></dl>
<h2>Author</h2>
<p>Red Hat, Inc</p>
<h2>Copyright</h2>
<p>2013, Red Hat, Inc</p>
