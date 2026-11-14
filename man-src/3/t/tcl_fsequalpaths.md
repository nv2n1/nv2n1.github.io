---
title: "tcl_fsequalpaths(3)"
name: "tcl_fsequalpaths"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_fsequalpaths/"
---

Tcl_FSRegister, Tcl_FSUnregister, Tcl_FSData, Tcl_FSMountsChanged, Tcl_FSGetFileSystemForPath, Tcl_FSGetPathType, Tcl_FSCopyFile, Tcl_FSCopyDirectory, Tcl_FSCreateDirectory, Tcl_FSDeleteFile, Tcl_FSRemoveDirectory, Tcl_FSRenameFile, Tcl_FSListVolumes, Tcl_FSEvalFile, Tcl_FSEvalFileEx, Tcl_FSLoadFile, Tcl_FSMatchInDirectory, Tcl_FSLink, Tcl_FSLstat, Tcl_FSUtime, Tcl_FSFileAttrsGet, Tcl_FSFileAttrsSet, Tcl_FSFileAttrStrings, Tcl_FSStat, Tcl_FSAccess, Tcl_FSOpenFileChannel, Tcl_FSGetCwd, Tcl_FSChdir, Tcl_FSPathSeparator, Tcl_FSJoinPath, Tcl_FSSplitPath, Tcl_FSEqualPaths, Tcl_FSGetNormalizedPath, Tcl_FSJoinToPath, Tcl_FSConvertToPathType, Tcl_FSGetInternalRep, Tcl_FSGetTranslatedPath, Tcl_FSGetTranslatedStringPath, Tcl_FSNewNativePath, Tcl_FSGetNativePath, Tcl_FSFileSystemInfo, Tcl_AllocStatBuf - procedures to interact with any filesystem 

<h2>Synopsis</h2><pre><b>#include &lt;tcl.h&gt;</b>
int
<b>Tcl_FSRegister</b>(<i>clientData, fsPtr</i>)
int
<b>Tcl_FSUnregister</b>(<i>fsPtr</i>)
ClientData
<b>Tcl_FSData</b>(<i>fsPtr</i>)
void
<b>Tcl_FSMountsChanged</b>(<i>fsPtr</i>)
Tcl_Filesystem*
<b>Tcl_FSGetFileSystemForPath</b>(<i>pathPtr</i>)
Tcl_PathType
<b>Tcl_FSGetPathType</b>(<i>pathPtr</i>)
int
<b>Tcl_FSCopyFile</b>(<i>srcPathPtr, destPathPtr</i>)
int
<b>Tcl_FSCopyDirectory</b>(<i>srcPathPtr, destPathPtr, errorPtr</i>)
int
<b>Tcl_FSCreateDirectory</b>(<i>pathPtr</i>)
int
<b>Tcl_FSDeleteFile</b>(<i>pathPtr</i>)
int
<b>Tcl_FSRemoveDirectory</b>(<i>pathPtr, int recursive, errorPtr</i>)
int
<b>Tcl_FSRenameFile</b>(<i>srcPathPtr, destPathPtr</i>)
Tcl_Obj*
<b>Tcl_FSListVolumes</b>(<i>void</i>)
int
<b>Tcl_FSEvalFileEx</b>(<i>interp, pathPtr, encodingName</i>)
int
<b>Tcl_FSEvalFile</b>(<i>interp, pathPtr</i>)
int
<b>Tcl_FSLoadFile</b>(<i>interp, pathPtr, sym1, sym2, proc1Ptr, proc2Ptr,
 handlePtr, unloadProcPtr</i>)
int
<b>Tcl_FSMatchInDirectory</b>(<i>interp, resultPtr, pathPtr, pattern, types</i>)
Tcl_Obj*
<b>Tcl_FSLink</b>(<i>linkNamePtr, toPtr, linkAction</i>)
int
<b>Tcl_FSLstat</b>(<i>pathPtr, statPtr</i>)
int
<b>Tcl_FSUtime</b>(<i>pathPtr, tval</i>)
int
<b>Tcl_FSFileAttrsGet</b>(<i>interp, int index, pathPtr, objPtrRef</i>)
int
<b>Tcl_FSFileAttrsSet</b>(<i>interp, int index, pathPtr, Tcl_Obj *objPtr</i>)
const char**
<b>Tcl_FSFileAttrStrings</b>(<i>pathPtr, objPtrRef</i>)
int
<b>Tcl_FSStat</b>(<i>pathPtr, statPtr</i>)
int
<b>Tcl_FSAccess</b>(<i>pathPtr, mode</i>)
Tcl_Channel
<b>Tcl_FSOpenFileChannel</b>(<i>interp, pathPtr, modeString, permissions</i>)
Tcl_Obj*
<b>Tcl_FSGetCwd</b>(<i>interp</i>)
int
<b>Tcl_FSChdir</b>(<i>pathPtr</i>)
Tcl_Obj*
<b>Tcl_FSPathSeparator</b>(<i>pathPtr</i>)
Tcl_Obj*
<b>Tcl_FSJoinPath</b>(<i>listObj, elements</i>)
Tcl_Obj*
<b>Tcl_FSSplitPath</b>(<i>pathPtr, lenPtr</i>)
int
<b>Tcl_FSEqualPaths</b>(<i>firstPtr, secondPtr</i>)
Tcl_Obj*
<b>Tcl_FSGetNormalizedPath</b>(<i>interp, pathPtr</i>)
Tcl_Obj*
<b>Tcl_FSJoinToPath</b>(<i>basePtr, objc, objv</i>)
int
<b>Tcl_FSConvertToPathType</b>(<i>interp, pathPtr</i>)
ClientData
<b>Tcl_FSGetInternalRep</b>(<i>pathPtr, fsPtr</i>)
Tcl_Obj *
<b>Tcl_FSGetTranslatedPath</b>(<i>interp, pathPtr</i>)
const char *
<b>Tcl_FSGetTranslatedStringPath</b>(<i>interp, pathPtr</i>)
Tcl_Obj*
<b>Tcl_FSNewNativePath</b>(<i>fsPtr, clientData</i>)
const char *
<b>Tcl_FSGetNativePath</b>(<i>pathPtr</i>)
Tcl_Obj*
<b>Tcl_FSFileSystemInfo</b>(<i>pathPtr</i>)
Tcl_StatBuf*
<b>Tcl_AllocStatBuf</b>()</pre><h2>Arguments</h2><dl COMPACT><dd>Tcl_Filesystem <i>*fsPtr</i> (in) Points to a structure containing the addresses of procedures that can be called to perform the various filesystem operations.
<dd>Tcl_Obj <i>*pathPtr</i> (in) The path represented by this object is used for the operation in question. If the object does not already have an internal <b>path</b> representation, it will be converted to have one.
<dd>Tcl_Obj <i>*srcPathPtr</i> (in) As for <i>pathPtr</i>, but used for the source file for a copy or rename operation.
<dd>Tcl_Obj <i>*destPathPtr</i> (in) As for <i>pathPtr</i>, but used for the destination filename for a copy or rename operation.
<dd>const char <i>*encodingName</i> (in) The encoding of the data stored in the file identified by <i>pathPtr</i> and to be evaluated.
<dd>const char <i>*pattern</i> (in) Only files or directories matching this pattern will be returned.
<dd>Tcl_GlobTypeData <i>*types</i> (in) Only files or directories matching the type descriptions contained in this structure will be returned. This parameter may be NULL.
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use either for results, evaluation, or reporting error messages.
<dd>ClientData <i>clientData</i> (in) The native description of the path object to create.
<dd>Tcl_Obj <i>*firstPtr</i> (in) The first of two path objects to compare. The object may be converted to <b>path</b> type.
<dd>Tcl_Obj <i>*secondPtr</i> (in) The second of two path objects to compare. The object may be converted to <b>path</b> type.
<dd>Tcl_Obj <i>*listObj</i> (in) The list of path elements to operate on with a <b>join</b> operation.
<dd>int <i>elements</i> (in) If non-negative, the number of elements in the <i>listObj</i> which should be joined together. If negative, then all elements are joined.
<dd>Tcl_Obj <i>**errorPtr</i> (out) In the case of an error, filled with an object containing the name of the file which caused an error in the various copy/rename operations.
<dd>Tcl_Obj <i>**objPtrRef</i> (out) Filled with an object containing the result of the operation.
<dd>Tcl_Obj <i>*resultPtr</i> (out) Pre-allocated object in which to store (using <b>Tcl_ListObjAppendElement</b>) the list of files or directories which are successfully matched.
<dd>int <i>mode</i> (in) Mask consisting of one or more of R_OK, W_OK, X_OK and F_OK. R_OK, W_OK and X_OK request checking whether the file exists and has read, write and execute permissions, respectively. F_OK just requests checking for the existence of the file.
<dd>Tcl_StatBuf <i>*statPtr</i> (out) The structure that contains the result of a stat or lstat operation.
<dd>const char <i>*sym1</i> (in) Name of a procedure to look up in the file's symbol table
<dd>const char <i>*sym2</i> (in) Name of a procedure to look up in the file's symbol table
<dd>Tcl_PackageInitProc <i>**proc1Ptr</i> (out) Filled with the init function for this code.
<dd>Tcl_PackageInitProc <i>**proc2Ptr</i> (out) Filled with the safe-init function for this code.
<dd>ClientData <i>*clientDataPtr</i> (out) Filled with the clientData value to pass to this code's unload function when it is called.
<dd>Tcl_LoadHandle <i>*handlePtr</i> (out) Filled with an abstract token representing the loaded file.
<dd>Tcl_FSUnloadFileProc <i>**unloadProcPtr</i> (out) Filled with the function to use to unload this piece of code.
<dd>utimbuf <i>*tval</i> (in) The access and modification times in this structure are read and used to set those values for a given file.
<dd>const char <i>*modeString</i> (in) Specifies how the file is to be accessed. May have any of the values allowed for the <i>mode</i> argument to the Tcl <b>open</b> command.
<dd>int <i>permissions</i> (in) POSIX-style permission flags such as 0644. If a new file is created, these permissions will be set on the created file.
<dd>int <i>*lenPtr</i> (out) If non-NULL, filled with the number of elements in the split path.
<dd>Tcl_Obj <i>*basePtr</i> (in) The base path on to which to join the given elements. May be NULL.
<dd>int <i>objc</i> (in) The number of elements in <i>objv</i>.
<dd>Tcl_Obj *const <i>objv[]</i> (in) The elements to join to the given base path.
<dd>Tcl_Obj <i>*linkNamePtr</i> (in) The name of the link to be created or read.
<dd>Tcl_Obj <i>*toPtr</i> (in) What the link called <i>linkNamePtr</i> should be linked to, or NULL if the symbolic link specified by <i>linkNamePtr</i> is to be read.
<dd>int <i>linkAction</i> (in) OR-ed combination of flags indicating what kind of link should be created (will be ignored if <i>toPtr</i> is NULL). Valid bits to set are <b>TCL_CREATE_SYMBOLIC_LINK</b> and <b>TCL_CREATE_HARD_LINK</b>. When both flags are set and the underlying filesystem can do either, symbolic links are preferred. 
 

</dl><h2>Description</h2>There are several reasons for calling the <b>Tcl_FS</b> API functions (e.g. <b>Tcl_FSAccess</b> and <b>Tcl_FSStat</b>) rather than calling system level functions like <b>access</b> and <b>stat</b> directly. First, they will work cross-platform, so an extension which calls them should work unmodified on Unix and Windows. Second, the Windows implementation of some of these functions fixes some bugs in the system level calls. Third, these function calls deal with any ``Utf to platform-native'' path conversions which may be required (and may cache the results of such conversions for greater efficiency on subsequent calls). Fourth, and perhaps most importantly, all of these functions are ``virtual filesystem aware''. Any virtual filesystem (VFS for short) which has been registered (through <b>Tcl_FSRegister</b>) may reroute file access to alternative media or access methods. This means that all of these functions (and therefore the corresponding <b>file</b>, <b>glob</b>, <b>pwd</b>, <b>cd</b>, <b>open</b>, etc. Tcl commands) may be operate on ``files'' which are not native files in the native filesystem. This also means that any Tcl extension which accesses the filesystem (FS for short) through this API is automatically ``virtual filesystem aware''. Of course, if an extension accesses the native filesystem directly (through platform-specific APIs, for example), then Tcl cannot intercept such calls. 

 If appropriate VFSes have been registered, the ``files'' may, to give two examples, be remote (e.g. situated on a remote ftp server) or archived (e.g. lying inside a .zip archive). Such registered filesystems provide a lookup table of functions to implement all or some of the functionality listed here. Finally, the <b>Tcl_FSStat</b> and <b>Tcl_FSLstat</b> calls abstract away from what the ``struct stat'' buffer is actually declared to be, allowing the same code to be used both on systems with and systems without support for files larger than 2GB in size. 

 The <b>Tcl_FS</b> API is objectified and may cache internal representations and other path-related strings (e.g. the current working directory). One side-effect of this is that one must not pass in objects with a reference count of zero to any of these functions. If such calls were handled, they might result in memory leaks (under some circumstances, the filesystem code may wish to retain a reference to the passed in object, and so one must not assume that after any of these calls return, the object still has a reference count of zero - it may have been incremented) or in a direct segmentation fault (or other memory access error) due to the object being freed part way through the complex object manipulation required to ensure that the path is fully normalized and absolute for filesystem determination. The practical lesson to learn from this is that
<dl COMPACT><dd><pre>Tcl_Obj *path = Tcl_NewStringObj(...);
Tcl_FS<i>Whatever</i>(path);
Tcl_DecrRefCount(path);</pre></dl>
 is wrong, and may cause memory errors. The <i>path</i> must have its reference count incremented before passing it in, or decrementing it. For this reason, objects with a reference count of zero are considered not to be valid filesystem paths and calling any Tcl_FS API function with such an object will result in no action being taken.
<h3>Fs Api Functions</h3><b>Tcl_FSCopyFile</b> attempts to copy the file given by <i>srcPathPtr</i> to the path name given by <i>destPathPtr</i>. If the two paths given lie in the same filesystem (according to <b>Tcl_FSGetFileSystemForPath</b>) then that filesystem's ``copy file'' function is called (if it is non-NULL). Otherwise the function returns -1 and sets the <b>errno</b> global C variable to the ``EXDEV'' POSIX error code (which signifies a ``cross-domain link''). 

 <b>Tcl_FSCopyDirectory</b> attempts to copy the directory given by <i>srcPathPtr</i> to the path name given by <i>destPathPtr</i>. If the two paths given lie in the same filesystem (according to <b>Tcl_FSGetFileSystemForPath</b>) then that filesystem's ``copy file'' function is called (if it is non-NULL). Otherwise the function returns -1 and sets the <b>errno</b> global C variable to the ``EXDEV'' POSIX error code (which signifies a ``cross-domain link''). 

 <b>Tcl_FSCreateDirectory</b> attempts to create the directory given by <i>pathPtr</i> by calling the owning filesystem's ``create directory'' function. 

 <b>Tcl_FSDeleteFile</b> attempts to delete the file given by <i>pathPtr</i> by calling the owning filesystem's ``delete file'' function. 

 <b>Tcl_FSRemoveDirectory</b> attempts to remove the directory given by <i>pathPtr</i> by calling the owning filesystem's ``remove directory'' function. 

 <b>Tcl_FSRenameFile</b> attempts to rename the file or directory given by <i>srcPathPtr</i> to the path name given by <i>destPathPtr</i>. If the two paths given lie in the same filesystem (according to <b>Tcl_FSGetFileSystemForPath</b>) then that filesystem's ``rename file'' function is called (if it is non-NULL). Otherwise the function returns -1 and sets the <b>errno</b> global C variable to the ``EXDEV'' POSIX error code (which signifies a ``cross-domain link''). 

 <b>Tcl_FSListVolumes</b> calls each filesystem which has a non-NULL ``list volumes'' function and asks them to return their list of root volumes. It accumulates the return values in a list which is returned to the caller (with a reference count of 0). 

 <b>Tcl_FSEvalFileEx</b> reads the file given by <i>pathPtr</i> using the encoding identified by <i>encodingName</i> and evaluates its contents as a Tcl script. It returns the same information as <b>Tcl_EvalObjEx</b>. If <i>encodingName</i> is NULL, the system encoding is used for reading the file contents. If the file could not be read then a Tcl error is returned to describe why the file could not be read. The eofchar for files is ``\32'' (^Z) for all platforms. If you require a ``^Z'' in code for string comparison, you can use ``\032'' or ``\u001a'', which will be safely substituted by the Tcl interpreter into ``^Z''. <b>Tcl_FSEvalFile</b> is a simpler version of <b>Tcl_FSEvalFileEx</b> that always uses the system encoding when reading the file. 

 <b>Tcl_FSLoadFile</b> dynamically loads a binary code file into memory and returns the addresses of two procedures within that file, if they are defined. The appropriate function for the filesystem to which <i>pathPtr</i> belongs will be called. If that filesystem does not implement this function (most virtual filesystems will not, because of OS limitations in dynamically loading binary code), Tcl will attempt to copy the file to a temporary directory and load that temporary file. 

 Returns a standard Tcl completion code. If an error occurs, an error message is left in the <i>interp</i>'s result. 

 <b>Tcl_FSMatchInDirectory</b> is used by the globbing code to search a directory for all files which match a given pattern. The appropriate function for the filesystem to which <i>pathPtr</i> belongs will be called. 

 The return value is a standard Tcl result indicating whether an error occurred in globbing. Error messages are placed in interp (unless interp is NULL, which is allowed), but good results are placed in the resultPtr given. 

 Note that the <b>glob</b> code implements recursive patterns internally, so this function will only ever be passed simple patterns, which can be matched using the logic of <b>string match</b>. To handle recursion, Tcl will call this function frequently asking only for directories to be returned. A special case of being called with a NULL pattern indicates that the path needs to be checked only for the correct type. 

 <b>Tcl_FSLink</b> replaces the library version of <b>readlink</b>, and extends it to support the creation of links. The appropriate function for the filesystem to which <i>linkNamePtr</i> belongs will be called. 

 If the <i>toPtr</i> is NULL, a ``read link'' action is performed. The result is a Tcl_Obj specifying the contents of the symbolic link given by <i>linkNamePtr</i>, or NULL if the link could not be read. The result is owned by the caller, which should call Tcl_DecrRefCount when the result is no longer needed. If the <i>toPtr</i> is not NULL, Tcl should create a link of one of the types passed in in the <i>linkAction</i> flag. This flag is an ORed combination of <b>TCL_CREATE_SYMBOLIC_LINK</b> and <b>TCL_CREATE_HARD_LINK</b>. Where a choice exists (i.e. more than one flag is passed in), the Tcl convention is to prefer symbolic links. When a link is successfully created, the return value should be <i>toPtr</i> (which is therefore already owned by the caller). If unsuccessful, NULL is returned. 

 <b>Tcl_FSLstat</b> fills the stat structure <i>statPtr</i> with information about the specified file. You do not need any access rights to the file to get this information but you need search rights to all directories named in the path leading to the file. The stat structure includes info regarding device, inode (always 0 on Windows), privilege mode, nlink (always 1 on Windows), user id (always 0 on Windows), group id (always 0 on Windows), rdev (same as device on Windows), size, last access time, last modification time, and last metadata change time. 

 If <i>path</i> exists, <b>Tcl_FSLstat</b> returns 0 and the stat structure is filled with data. Otherwise, -1 is returned, and no stat info is given. 

 <b>Tcl_FSUtime</b> replaces the library version of utime. 

 This returns 0 on success and -1 on error (as per the <b>utime</b> documentation). If successful, the function will update the ``atime'' and ``mtime'' values of the file given. 

 <b>Tcl_FSFileAttrsGet</b> implements read access for the hookable <b>file attributes</b> subcommand. The appropriate function for the filesystem to which <i>pathPtr</i> belongs will be called. 

 If the result is <b>TCL_OK</b>, then an object was placed in <i>objPtrRef</i>, which will only be temporarily valid (unless <b>Tcl_IncrRefCount</b> is called). 

 <b>Tcl_FSFileAttrsSet</b> implements write access for the hookable <b>file attributes</b> subcommand. The appropriate function for the filesystem to which <i>pathPtr</i> belongs will be called. 

 <b>Tcl_FSFileAttrStrings</b> implements part of the hookable <b>file attributes</b> subcommand. The appropriate function for the filesystem to which <i>pathPtr</i> belongs will be called. 

 The called procedure may either return an array of strings, or may instead return NULL and place a Tcl list into the given <i>objPtrRef</i>. Tcl will take that list and first increment its reference count before using it. On completion of that use, Tcl will decrement its reference count. Hence if the list should be disposed of by Tcl when done, it should have a reference count of zero, and if the list should not be disposed of, the filesystem should ensure it retains a reference count to the object. 

 <b>Tcl_FSAccess</b> checks whether the process would be allowed to read, write or test for existence of the file (or other filesystem object) whose name is <i>pathname</i>. If <i>pathname</i> is a symbolic link on Unix, then permissions of the file referred by this symbolic link are tested. 

 On success (all requested permissions granted), zero is returned. On error (at least one bit in mode asked for a permission that is denied, or some other error occurred), -1 is returned. 

 <b>Tcl_FSStat</b> fills the stat structure <i>statPtr</i> with information about the specified file. You do not need any access rights to the file to get this information but you need search rights to all directories named in the path leading to the file. The stat structure includes info regarding device, inode (always 0 on Windows), privilege mode, nlink (always 1 on Windows), user id (always 0 on Windows), group id (always 0 on Windows), rdev (same as device on Windows), size, last access time, last modification time, and last metadata change time. 

 If <i>path</i> exists, <b>Tcl_FSStat</b> returns 0 and the stat structure is filled with data. Otherwise, -1 is returned, and no stat info is given. 

 <b>Tcl_FSOpenFileChannel</b> opens a file specified by <i>pathPtr</i> and returns a channel handle that can be used to perform input and output on the file. This API is modeled after the <b>fopen</b> procedure of the Unix standard I/O library. The syntax and meaning of all arguments is similar to those given in the Tcl <b>open</b> command when opening a file. If an error occurs while opening the channel, <b>Tcl_FSOpenFileChannel</b> returns NULL and records a POSIX error code that can be retrieved with <b>Tcl_GetErrno</b>. In addition, if <i>interp</i> is non-NULL, <b>Tcl_FSOpenFileChannel</b> leaves an error message in <i>interp</i>'s result after any error. 

 The newly created channel is not registered in the supplied interpreter; to register it, use <b>Tcl_RegisterChannel</b>. If one of the standard channels, <b>stdin, stdout</b> or <b>stderr</b> was previously closed, the act of creating the new channel also assigns it as a replacement for the standard channel. 

 <b>Tcl_FSGetCwd</b> replaces the library version of <b>getcwd</b>. 

 It returns the Tcl library's current working directory. This may be different to the native platform's working directory, which happens when the current working directory is not in the native filesystem. 

 The result is a pointer to a Tcl_Obj specifying the current directory, or NULL if the current directory could not be determined. If NULL is returned, an error message is left in the <i>interp</i>'s result. 

 The result already has its reference count incremented for the caller. When it is no longer needed, that reference count should be decremented. This is needed for thread-safety purposes, to allow multiple threads to access this and related functions, while ensuring the results are always valid. 

 <b>Tcl_FSChdir</b> replaces the library version of <b>chdir</b>. The path is normalized and then passed to the filesystem which claims it. If that filesystem does not implement this function, Tcl will fallback to a combination of <b>stat</b> and <b>access</b> to check whether the directory exists and has appropriate permissions. 

 For results, see <b>chdir</b> documentation. If successful, we keep a record of the successful path in <i>cwdPathPtr</i> for subsequent calls to <b>Tcl_FSGetCwd</b>. 

 <b>Tcl_FSPathSeparator</b> returns the separator character to be used for most specific element of the path specified by <i>pathPtr</i> (i.e. the last part of the path). 

 The separator is returned as a Tcl_Obj containing a string of length 1. If the path is invalid, NULL is returned. 

 <b>Tcl_FSJoinPath</b> takes the given Tcl_Obj, which must be a valid list (which is allowed to have a reference count of zero), and returns the path object given by considering the first <i>elements</i> elements as valid path segments (each path segment may be a complete path, a partial path or just a single possible directory or file name). If any path segment is actually an absolute path, then all prior path segments are discarded. If <i>elements</i> is less than 0, we use the entire list. 

 It is possible that the returned object is actually an element of the given list, so the caller should be careful to increment the reference count of the result before freeing the list. 

 The returned object, typically with a reference count of zero (but it could be shared under some conditions), contains the joined path. The caller must add a reference count to the object before using it. In particular, the returned object could be an element of the given list, so freeing the list might free the object prematurely if no reference count has been taken. If the number of elements is zero, then the returned object will be an empty-string Tcl_Obj. 

 <b>Tcl_FSSplitPath</b> takes the given Tcl_Obj, which should be a valid path, and returns a Tcl list object containing each segment of that path as an element. It returns a list object with a reference count of zero. If the passed in <i>lenPtr</i> is non-NULL, the variable it points to will be updated to contain the number of elements in the returned list. 

 <b>Tcl_FSEqualPaths</b> tests whether the two paths given represent the same filesystem object 

 It returns 1 if the paths are equal, and 0 if they are different. If either path is NULL, 0 is always returned. 

 <b>Tcl_FSGetNormalizedPath</b> this important function attempts to extract from the given Tcl_Obj a unique normalized path representation, whose string value can be used as a unique identifier for the file. 

 It returns the normalized path object, owned by Tcl, or NULL if the path was invalid or could otherwise not be successfully converted. Extraction of absolute, normalized paths is very efficient (because the filesystem operates on these representations internally), although the result when the filesystem contains numerous symbolic links may not be the most user-friendly version of a path. The return value is owned by Tcl and has a lifetime equivalent to that of the <i>pathPtr</i> passed in (unless that is a relative path, in which case the normalized path object may be freed any time the cwd changes) - the caller can of course increment the refCount if it wishes to maintain a copy for longer. 

 <b>Tcl_FSJoinToPath</b> takes the given object, which should usually be a valid path or NULL, and joins onto it the array of paths segments given. 

 Returns object, typically with refCount of zero (but it could be shared under some conditions), containing the joined path. The caller must add a refCount to the object before using it. If any of the objects passed into this function (pathPtr or path elements) have a refCount of zero, they will be freed when this function returns. 

 <b>Tcl_FSConvertToPathType</b> tries to convert the given Tcl_Obj to a valid Tcl path type, taking account of the fact that the cwd may have changed even if this object is already supposedly of the correct type. The filename may begin with ``~'' (to indicate current user's home directory) or ``~&lt;user&gt;'' (to indicate any user's home directory). 

 If the conversion succeeds (i.e. the object is a valid path in one of the current filesystems), then <b>TCL_OK</b> is returned. Otherwise <b>TCL_ERROR</b> is returned, and an error message may be left in the interpreter. 

 <b>Tcl_FSGetInternalRep</b> extracts the internal representation of a given path object, in the given filesystem. If the path object belongs to a different filesystem, we return NULL. If the internal representation is currently NULL, we attempt to generate it, by calling the filesystem's <b>Tcl_FSCreateInternalRepProc</b>. 

 Returns NULL or a valid internal path representation. This internal representation is cached, so that repeated calls to this function will not require additional conversions. 

 <b>Tcl_FSGetTranslatedPath</b> attempts to extract the translated path from the given Tcl_Obj. 

 If the translation succeeds (i.e. the object is a valid path), then it is returned. Otherwise NULL will be returned, and an error message may be left in the interpreter. A ``translated'' path is one which contains no ``~'' or ``~user'' sequences (these have been expanded to their current representation in the filesystem). The object returned is owned by the caller, which must store it or call Tcl_DecrRefCount to ensure memory is freed. This function is of little practical use, and <b>Tcl_FSGetNormalizedPath</b> or <b>Tcl_GetNativePath</b> are usually better functions to use for most purposes. 

 <b>Tcl_FSGetTranslatedStringPath</b> does the same as <b>Tcl_FSGetTranslatedPath</b>, but returns a character string or NULL. The string returned is dynamically allocated and owned by the caller, which must store it or call <b>ckfree</b> to ensure it is freed. Again, <b>Tcl_FSGetNormalizedPath</b> or <b>Tcl_GetNativePath</b> are usually better functions to use for most purposes. 

 <b>Tcl_FSNewNativePath</b> performs something like the reverse of the usual obj-&gt;path-&gt;nativerep conversions. If some code retrieves a path in native form (from, e.g. <b>readlink</b> or a native dialog), and that path is to be used at the Tcl level, then calling this function is an efficient way of creating the appropriate path object type. 

 The resulting object is a pure ``path'' object, which will only receive a UTF-8 string representation if that is required by some Tcl code. 

 <b>Tcl_FSGetNativePath</b> is for use by the Win/Unix native filesystems, so that they can easily retrieve the native (char* or TCHAR*) representation of a path. This function is a convenience wrapper around <b>Tcl_FSGetInternalRep</b>, and assumes the native representation is string-based. It may be desirable in the future to have non-string-based native representations (for example, on MacOSX, a representation using a fileSpec of FSRef structure would probably be more efficient). On Windows a full Unicode representation would allow for paths of unlimited length. Currently the representation is simply a character string which may contain either the relative path or a complete, absolute normalized path in the native encoding (complex conditions dictate which of these will be provided, so neither can be relied upon, unless the path is known to be absolute). If you need a native path which must be absolute, then you should ask for the native version of a normalized path. If for some reason a non-absolute, non-normalized version of the path is needed, that must be constructed separately (e.g. using <b>Tcl_FSGetTranslatedPath</b>). 

 The native representation is cached so that repeated calls to this function will not require additional conversions. The return value is owned by Tcl and has a lifetime equivalent to that of the <i>pathPtr</i> passed in (unless that is a relative path, in which case the native representation may be freed any time the cwd changes). 

 <b>Tcl_FSFileSystemInfo</b> returns a list of two elements. The first element is the name of the filesystem (e.g. ``native'', ``vfs'', ``zip'', or ``prowrap'', perhaps), and the second is the particular type of the given path within that filesystem (which is filesystem dependent). The second element may be empty if the filesystem does not provide a further categorization of files. 

 A valid list object is returned, unless the path object is not recognized, when NULL will be returned. 

 <b>Tcl_FSGetFileSystemForPath</b> returns the a pointer to the <b>Tcl_Filesystem</b> which accepts this path as valid. 

 If no filesystem will accept the path, NULL is returned. 

 <b>Tcl_FSGetPathType</b> determines whether the given path is relative to the current directory, relative to the current volume, or absolute. 

 It returns one of <b>TCL_PATH_ABSOLUTE</b>, <b>TCL_PATH_RELATIVE</b>, or <b>TCL_PATH_VOLUME_RELATIVE</b> 

 <b>Tcl_AllocStatBuf</b> allocates a <i>Tcl_StatBuf</i> on the system heap (which may be deallocated by being passed to <b>ckfree</b>.) This allows extensions to invoke <b>Tcl_FSStat</b> and <b>Tcl_FSLStat</b> without being dependent on the size of the buffer. That in turn depends on the flags used to build Tcl.
<h2>The Virtual Filesystem Api</h2>A filesystem provides a <b>Tcl_Filesystem</b> structure that contains pointers to functions that implement the various operations on a filesystem; these operations are invoked as needed by the generic layer, which generally occurs through the functions listed above. 

 The <b>Tcl_Filesystem</b> structures are manipulated using the following methods. 

 <b>Tcl_FSRegister</b> takes a pointer to a filesystem structure and an optional piece of data to associated with that filesystem. On calling this function, Tcl will attach the filesystem to the list of known filesystems, and it will become fully functional immediately. Tcl does not check if the same filesystem is registered multiple times (and in general that is not a good thing to do). <b>TCL_OK</b> will be returned. 

 <b>Tcl_FSUnregister</b> removes the given filesystem structure from the list of known filesystems, if it is known, and returns <b>TCL_OK</b>. If the filesystem is not currently registered, <b>TCL_ERROR</b> is returned. 

 <b>Tcl_FSData</b> will return the ClientData associated with the given filesystem, if that filesystem is registered. Otherwise it will return NULL. 

 <b>Tcl_FSMountsChanged</b> is used to inform the Tcl's core that the set of mount points for the given (already registered) filesystem have changed, and that cached file representations may therefore no longer be correct.
<h3>The Tcl_Filesystem Structure</h3>The <b>Tcl_Filesystem</b> structure contains the following fields:
<dl COMPACT><dd><pre>typedef struct Tcl_Filesystem {
 const char *<i>typeName</i>;
 int <i>structureLength</i>;
 Tcl_FSVersion <i>version</i>;
 Tcl_FSPathInFilesystemProc *<i>pathInFilesystemProc</i>;
 Tcl_FSDupInternalRepProc *<i>dupInternalRepProc</i>;
 Tcl_FSFreeInternalRepProc *<i>freeInternalRepProc</i>;
 Tcl_FSInternalToNormalizedProc *<i>internalToNormalizedProc</i>;
 Tcl_FSCreateInternalRepProc *<i>createInternalRepProc</i>;
 Tcl_FSNormalizePathProc *<i>normalizePathProc</i>;
 Tcl_FSFilesystemPathTypeProc *<i>filesystemPathTypeProc</i>;
 Tcl_FSFilesystemSeparatorProc *<i>filesystemSeparatorProc</i>;
 Tcl_FSStatProc *<i>statProc</i>;
 Tcl_FSAccessProc *<i>accessProc</i>;
 Tcl_FSOpenFileChannelProc *<i>openFileChannelProc</i>;
 Tcl_FSMatchInDirectoryProc *<i>matchInDirectoryProc</i>;
 Tcl_FSUtimeProc *<i>utimeProc</i>;
 Tcl_FSLinkProc *<i>linkProc</i>;
 Tcl_FSListVolumesProc *<i>listVolumesProc</i>;
 Tcl_FSFileAttrStringsProc *<i>fileAttrStringsProc</i>;
 Tcl_FSFileAttrsGetProc *<i>fileAttrsGetProc</i>;
 Tcl_FSFileAttrsSetProc *<i>fileAttrsSetProc</i>;
 Tcl_FSCreateDirectoryProc *<i>createDirectoryProc</i>;
 Tcl_FSRemoveDirectoryProc *<i>removeDirectoryProc</i>;
 Tcl_FSDeleteFileProc *<i>deleteFileProc</i>;
 Tcl_FSCopyFileProc *<i>copyFileProc</i>;
 Tcl_FSRenameFileProc *<i>renameFileProc</i>;
 Tcl_FSCopyDirectoryProc *<i>copyDirectoryProc</i>;
 Tcl_FSLstatProc *<i>lstatProc</i>;
 Tcl_FSLoadFileProc *<i>loadFileProc</i>;
 Tcl_FSGetCwdProc *<i>getCwdProc</i>;
 Tcl_FSChdirProc *<i>chdirProc</i>;
} Tcl_Filesystem;</pre></dl>
 

 Except for the first three fields in this structure which contain simple data elements, all entries contain addresses of functions called by the generic filesystem layer to perform the complete range of filesystem related actions. 

 The many functions in this structure are broken down into three categories: infrastructure functions (almost all of which must be implemented), operational functions (which must be implemented if a complete filesystem is provided), and efficiency functions (which need only be implemented if they can be done so efficiently, or if they have side-effects which are required by the filesystem; Tcl has less efficient emulations it can fall back on). It is important to note that, in the current version of Tcl, most of these fallbacks are only used to handle commands initiated in Tcl, not in C. What this means is, that if a <b>file rename</b> command is issued in Tcl, and the relevant filesystem(s) do not implement their <i>Tcl_FSRenameFileProc</i>, Tcl's core will instead fallback on a combination of other filesystem functions (it will use <i>Tcl_FSCopyFileProc</i> followed by <i>Tcl_FSDeleteFileProc</i>, and if <i>Tcl_FSCopyFileProc</i> is not implemented there is a further fallback). However, if a <i>Tcl_FSRenameFileProc</i> command is issued at the C level, no such fallbacks occur. This is true except for the last four entries in the filesystem table (<b>lstat</b>, <b>load</b>, <b>getcwd</b> and <b>chdir</b>) for which fallbacks do in fact occur at the C level. 

 Any functions which take path names in Tcl_Obj form take those names in UTF-8 form. The filesystem infrastructure API is designed to support efficient, cached conversion of these UTF-8 paths to other native representations.
<h3>Example Filesystem Definition</h3>Here is the filesystem lookup table used by the ``vfs'' extension which allows filesystem actions to be implemented in Tcl.
<dl COMPACT><dd><pre>static Tcl_Filesystem vfsFilesystem = {
 &quot;tclvfs&quot;,
 sizeof(Tcl_Filesystem),
 TCL_FILESYSTEM_VERSION_1,
 &amp;VfsPathInFilesystem,
 &amp;VfsDupInternalRep,
 &amp;VfsFreeInternalRep,
 /* No internal to normalized, since we don't create
 * any pure 'internal' Tcl_Obj path representations */
 NULL,
 /* No create native rep function, since we don't use
 * it and don't choose to support uses of
 * Tcl_FSNewNativePath */
 NULL,
 /* Normalize path isn't needed - we assume paths only
 * have one representation */
 NULL,
 &amp;VfsFilesystemPathType,
 &amp;VfsFilesystemSeparator,
 &amp;VfsStat,
 &amp;VfsAccess,
 &amp;VfsOpenFileChannel,
 &amp;VfsMatchInDirectory,
 &amp;VfsUtime,
 /* We choose not to support symbolic links inside our
 * VFS's */
 NULL,
 &amp;VfsListVolumes,
 &amp;VfsFileAttrStrings,
 &amp;VfsFileAttrsGet,
 &amp;VfsFileAttrsSet,
 &amp;VfsCreateDirectory,
 &amp;VfsRemoveDirectory,
 &amp;VfsDeleteFile,
 /* No copy file; use the core fallback mechanism */
 NULL,
 /* No rename file; use the core fallback mechanism */
 NULL,
 /* No copy directory; use the core fallback mechanism */
 NULL,
 /* Core will use stat for lstat */
 NULL,
 /* No load; use the core fallback mechanism */
 NULL,
 /* We don't need a getcwd or chdir; the core's own
 * internal value is suitable */
 NULL,
 NULL
};</pre></dl><h2>Filesystem Infrastructure</h2>These fields contain basic information about the filesystem structure and addresses of functions which are used to associate a particular filesystem with a file path, and deal with the internal handling of path representations, for example copying and freeing such representations.
<h3>Typename</h3>The <i>typeName</i> field contains a null-terminated string that identifies the type of the filesystem implemented, e.g. ``native'', ``zip'' or ``vfs''.
<h3>Structure Length</h3>The <i>structureLength</i> field is generally implemented as <i>sizeof(Tcl_Filesystem)</i>, and is there to allow easier binary backwards compatibility if the size of the structure changes in a future Tcl release.
<h3>Version</h3>The <i>version</i> field should be set to <b>TCL_FILESYSTEM_VERSION_1</b>.
<h3>Pathinfilesystemproc</h3>The <i>pathInFilesystemProc</i> field contains the address of a function which is called to determine whether a given path object belongs to this filesystem or not. Tcl will only call the rest of the filesystem functions with a path for which this function has returned <b>TCL_OK</b>. If the path does not belong, -1 should be returned (the behaviour of Tcl for any other return value is not defined). If <b>TCL_OK</b> is returned, then the optional <i>clientDataPtr</i> output parameter can be used to return an internal (filesystem specific) representation of the path, which will be cached inside the path object, and may be retrieved efficiently by the other filesystem functions. Tcl will simultaneously cache the fact that this path belongs to this filesystem. Such caches are invalidated when filesystem structures are added or removed from Tcl's internal list of known filesystems. 

<dl COMPACT><dd><pre>typedef int Tcl_FSPathInFilesystemProc(
 Tcl_Obj *<i>pathPtr</i>,
 ClientData *<i>clientDataPtr</i>);</pre></dl><h3>Dupinternalrepproc</h3>This function makes a copy of a path's internal representation, and is called when Tcl needs to duplicate a path object. If NULL, Tcl will simply not copy the internal representation, which may then need to be regenerated later. 

<dl COMPACT><dd><pre>typedef ClientData Tcl_FSDupInternalRepProc(
 ClientData <i>clientData</i>);</pre></dl><h3>Freeinternalrepproc</h3>Free the internal representation. This must be implemented if internal representations need freeing (i.e. if some memory is allocated when an internal representation is generated), but may otherwise be NULL. 

<dl COMPACT><dd><pre>typedef void Tcl_FSFreeInternalRepProc(
 ClientData <i>clientData</i>);</pre></dl><h3>Internaltonormalizedproc</h3>Function to convert internal representation to a normalized path. Only required if the filesystem creates pure path objects with no string/path representation. The return value is a Tcl object whose string representation is the normalized path. 

<dl COMPACT><dd><pre>typedef Tcl_Obj* Tcl_FSInternalToNormalizedProc(
 ClientData <i>clientData</i>);</pre></dl><h3>Createinternalrepproc</h3>Function to take a path object, and calculate an internal representation for it, and store that native representation in the object. May be NULL if paths have no internal representation, or if the <i>Tcl_FSPathInFilesystemProc</i> for this filesystem always immediately creates an internal representation for paths it accepts. 

<dl COMPACT><dd><pre>typedef ClientData Tcl_FSCreateInternalRepProc(
 Tcl_Obj *<i>pathPtr</i>);</pre></dl><h3>Normalizepathproc</h3>Function to normalize a path. Should be implemented for all filesystems which can have multiple string representations for the same path object. In Tcl, every ``path'' must have a single unique ``normalized'' string representation. Depending on the filesystem, there may be more than one unnormalized string representation which refers to that path (e.g. a relative path, a path with different character case if the filesystem is case insensitive, a path contain a reference to a home directory such as ``~'', a path containing symbolic links, etc). If the very last component in the path is a symbolic link, it should not be converted into the object it points to (but its case or other aspects should be made unique). All other path components should be converted from symbolic links. This one exception is required to agree with Tcl's semantics with <b>file delete</b>, <b>file rename</b>, <b>file copy</b> operating on symbolic links. This function may be called with <i>nextCheckpoint</i> either at the beginning of the path (i.e. zero), at the end of the path, or at any intermediate file separator in the path. It will never point to any other arbitrary position in the path. In the last of the three valid cases, the implementation can assume that the path up to and including the file separator is known and normalized. 

<dl COMPACT><dd><pre>typedef int Tcl_FSNormalizePathProc(
 Tcl_Interp *<i>interp</i>,
 Tcl_Obj *<i>pathPtr</i>,
 int <i>nextCheckpoint</i>);</pre></dl><h2>Filesystem Operations</h2>The fields in this section of the structure contain addresses of functions which are called to carry out the basic filesystem operations. A filesystem which expects to be used with the complete standard Tcl command set must implement all of these. If some of them are not implemented, then certain Tcl commands may fail when operating on paths within that filesystem. However, in some instances this may be desirable (for example, a read-only filesystem should not implement the last four functions, and a filesystem which does not support symbolic links need not implement the <b>readlink</b> function, etc. The Tcl core expects filesystems to behave in this way).
<h3>Filesystempathtypeproc</h3>Function to determine the type of a path in this filesystem. May be NULL, in which case no type information will be available to users of the filesystem. The ``type'' is used only for informational purposes, and should be returned as the string representation of the Tcl_Obj which is returned. A typical return value might be ``networked'', ``zip'' or ``ftp''. The Tcl_Obj result is owned by the filesystem and so Tcl will increment the refCount of that object if it wishes to retain a reference to it. 

<dl COMPACT><dd><pre>typedef Tcl_Obj* Tcl_FSFilesystemPathTypeProc(
 Tcl_Obj *<i>pathPtr</i>);</pre></dl><h3>Filesystemseparatorproc</h3>Function to return the separator character(s) for this filesystem. This need only be implemented if the filesystem wishes to use a different separator than the standard string ``/''. Amongst other uses, it is returned by the <b>file separator</b> command. The return value should be an object with refCount of zero. 

<dl COMPACT><dd><pre>typedef Tcl_Obj* Tcl_FSFilesystemSeparatorProc(
 Tcl_Obj *<i>pathPtr</i>);</pre></dl><h3>Statproc</h3>Function to process a <b>Tcl_FSStat</b> call. Must be implemented for any reasonable filesystem, since many Tcl level commands depend crucially upon it (e.g. <b>file atime</b>, <b>file isdirectory</b>, <b>file size</b>, <b>glob</b>). 

<dl COMPACT><dd><pre>typedef int Tcl_FSStatProc(
 Tcl_Obj *<i>pathPtr</i>,
 Tcl_StatBuf *<i>statPtr</i>);</pre></dl>
 

 The <b>Tcl_FSStatProc</b> fills the stat structure <i>statPtr</i> with information about the specified file. You do not need any access rights to the file to get this information but you need search rights to all directories named in the path leading to the file. The stat structure includes info regarding device, inode (always 0 on Windows), privilege mode, nlink (always 1 on Windows), user id (always 0 on Windows), group id (always 0 on Windows), rdev (same as device on Windows), size, last access time, last modification time, and last metadata change time. 

 If the file represented by <i>pathPtr</i> exists, the <b>Tcl_FSStatProc</b> returns 0 and the stat structure is filled with data. Otherwise, -1 is returned, and no stat info is given.
<h3>Accessproc</h3>Function to process a <b>Tcl_FSAccess</b> call. Must be implemented for any reasonable filesystem, since many Tcl level commands depend crucially upon it (e.g. <b>file exists</b>, <b>file readable</b>). 

<dl COMPACT><dd><pre>typedef int Tcl_FSAccessProc(
 Tcl_Obj *<i>pathPtr</i>,
 int <i>mode</i>);</pre></dl>
 

 The <b>Tcl_FSAccessProc</b> checks whether the process would be allowed to read, write or test for existence of the file (or other filesystem object) whose name is in <i>pathPtr</i>. If the pathname refers to a symbolic link, then the permissions of the file referred by this symbolic link should be tested. 

 On success (all requested permissions granted), zero is returned. On error (at least one bit in mode asked for a permission that is denied, or some other error occurred), -1 is returned.
<h3>Openfilechannelproc</h3>Function to process a <b>Tcl_FSOpenFileChannel</b> call. Must be implemented for any reasonable filesystem, since any operations which require open or accessing a file's contents will use it (e.g. <b>open</b>, <b>encoding</b>, and many Tk commands). 

<dl COMPACT><dd><pre>typedef Tcl_Channel Tcl_FSOpenFileChannelProc(
 Tcl_Interp *<i>interp</i>,
 Tcl_Obj *<i>pathPtr</i>,
 int <i>mode</i>,
 int <i>permissions</i>);</pre></dl>
 

 The <b>Tcl_FSOpenFileChannelProc</b> opens a file specified by <i>pathPtr</i> and returns a channel handle that can be used to perform input and output on the file. This API is modeled after the <b>fopen</b> procedure of the Unix standard I/O library. The syntax and meaning of all arguments is similar to those given in the Tcl <b>open</b> command when opening a file, where the <i>mode</i> argument is a combination of the POSIX flags O_RDONLY, O_WRONLY, etc. If an error occurs while opening the channel, the <b>Tcl_FSOpenFileChannelProc</b> returns NULL and records a POSIX error code that can be retrieved with <b>Tcl_GetErrno</b>. In addition, if <i>interp</i> is non-NULL, the <b>Tcl_FSOpenFileChannelProc</b> leaves an error message in <i>interp</i>'s result after any error. 

 The newly created channel must not registered in the supplied interpreter; that task is up to the caller of <b>Tcl_FSOpenFileChannel</b> (if necessary). If one of the standard channels, <b>stdin, stdout</b> or <b>stderr</b> was previously closed, the act of creating the new channel also assigns it as a replacement for the standard channel.
<h3>Matchindirectoryproc</h3>Function to process a <b>Tcl_FSMatchInDirectory</b> call. If not implemented, then glob and recursive copy functionality will be lacking in the filesystem (and this may impact commands like <b>encoding names</b> which use glob functionality internally). 

<dl COMPACT><dd><pre>typedef int Tcl_FSMatchInDirectoryProc(
 Tcl_Interp* <i>interp</i>,
 Tcl_Obj *<i>resultPtr</i>,
 Tcl_Obj *<i>pathPtr</i>,
 const char *<i>pattern</i>,
 Tcl_GlobTypeData *<i>types</i>);</pre></dl>
 

 The function should return all files or directories (or other filesystem objects) which match the given pattern and accord with the <i>types</i> specification given. There are two ways in which this function may be called. If <i>pattern</i> is NULL, then <i>pathPtr</i> is a full path specification of a single file or directory which should be checked for existence and correct type. Otherwise, <i>pathPtr</i> is a directory, the contents of which the function should search for files or directories which have the correct type. In either case, <i>pathPtr</i> can be assumed to be both non-NULL and non-empty. It is not currently documented whether <i>pathPtr</i> will have a file separator at its end of not, so code should be flexible to both possibilities. 

 The return value is a standard Tcl result indicating whether an error occurred in the matching process. Error messages are placed in <i>interp</i>, unless <i>interp</i> in NULL in which case no error message need be generated; on a <b>TCL_OK</b> result, results should be added to the <i>resultPtr</i> object given (which can be assumed to be a valid unshared Tcl list). The matches added to <i>resultPtr</i> should include any path prefix given in <i>pathPtr</i> (this usually means they will be absolute path specifications). Note that if no matches are found, that simply leads to an empty result; errors are only signaled for actual file or filesystem problems which may occur during the matching process. 

 The <b>Tcl_GlobTypeData</b> structure passed in the <i>types</i> parameter contains the following fields:
<dl COMPACT><dd><pre>typedef struct Tcl_GlobTypeData {
 /* Corresponds to bcdpfls as in 'find -t' */
 int <i>type</i>;
 /* Corresponds to file permissions */
 int <i>perm</i>;
 /* Acceptable mac type */
 Tcl_Obj *<i>macType</i>;
 /* Acceptable mac creator */
 Tcl_Obj *<i>macCreator</i>;
} Tcl_GlobTypeData;</pre></dl>
 

 There are two specific cases which it is important to handle correctly, both when <i>types</i> is non-NULL. The two cases are when <i>types-&gt;types &amp; TCL_GLOB_TYPE_DIR</i> or <i>types-&gt;types &amp; TCL_GLOB_TYPE_MOUNT</i> are true (and in particular when the other flags are false). In the first of these cases, the function must list the contained directories. Tcl uses this to implement recursive globbing, so it is critical that filesystems implement directory matching correctly. In the second of these cases, with <b>TCL_GLOB_TYPE_MOUNT</b>, the filesystem must list the mount points which lie within the given <i>pathPtr</i> (and in this case, <i>pathPtr</i> need not lie within the same filesystem - different to all other cases in which this function is called). Support for this is critical if Tcl is to have seamless transitions between from one filesystem to another.
<h3>Utimeproc</h3>Function to process a <b>Tcl_FSUtime</b> call. Required to allow setting (not reading) of times with <b>file mtime</b>, <b>file atime</b> and the open-r/open-w/fcopy implementation of <b>file copy</b>. 

<dl COMPACT><dd><pre>typedef int Tcl_FSUtimeProc(
 Tcl_Obj *<i>pathPtr</i>,
 struct utimbuf *<i>tval</i>);</pre></dl>
 

 The access and modification times of the file specified by <i>pathPtr</i> should be changed to the values given in the <i>tval</i> structure. 

 The return value should be 0 on success and -1 on an error, as with the system <b>utime</b>.
<h3>Linkproc</h3>Function to process a <b>Tcl_FSLink</b> call. Should be implemented only if the filesystem supports links, and may otherwise be NULL. 

<dl COMPACT><dd><pre>typedef Tcl_Obj* Tcl_FSLinkProc(
 Tcl_Obj *<i>linkNamePtr</i>,
 Tcl_Obj *<i>toPtr</i>,
 int <i>linkAction</i>);</pre></dl>
 

 If <i>toPtr</i> is NULL, the function is being asked to read the contents of a link. The result is a Tcl_Obj specifying the contents of the link given by <i>linkNamePtr</i>, or NULL if the link could not be read. The result is owned by the caller (and should therefore have its ref count incremented before being returned). Any callers should call Tcl_DecrRefCount on this result when it is no longer needed. If <i>toPtr</i> is not NULL, the function should attempt to create a link. The result in this case should be <i>toPtr</i> if the link was successful and NULL otherwise. In this case the result is not owned by the caller (i.e. no ref count manipulation on either end is needed). See the documentation for <b>Tcl_FSLink</b> for the correct interpretation of the <i>linkAction</i> flags.
<h3>Listvolumesproc</h3>Function to list any filesystem volumes added by this filesystem. Should be implemented only if the filesystem adds volumes at the head of the filesystem, so that they can be returned by <b>file volumes</b>. 

<dl COMPACT><dd><pre>typedef Tcl_Obj* Tcl_FSListVolumesProc(void);</pre></dl>
 

 The result should be a list of volumes added by this filesystem, or NULL (or an empty list) if no volumes are provided. The result object is considered to be owned by the filesystem (not by Tcl's core), but should be given a refCount for Tcl. Tcl will use the contents of the list and then decrement that refCount. This allows filesystems to choose whether they actually want to retain a ``master list'' of volumes or not (if not, they generate the list on the fly and pass it to Tcl with a refCount of 1 and then forget about the list, if yes, then they simply increment the refCount of their master list and pass it to Tcl which will copy the contents and then decrement the count back to where it was). 

 Therefore, Tcl considers return values from this proc to be read-only.
<h3>Fileattrstringsproc</h3>Function to list all attribute strings which are valid for this filesystem. If not implemented the filesystem will not support the <b>file attributes</b> command. This allows arbitrary additional information to be attached to files in the filesystem. If it is not implemented, there is no need to implement the <b>get</b> and <b>set</b> methods. 

<dl COMPACT><dd><pre>typedef const char** Tcl_FSFileAttrStringsProc(
 Tcl_Obj *<i>pathPtr</i>,
 Tcl_Obj** <i>objPtrRef</i>);</pre></dl>
 

 The called function may either return an array of strings, or may instead return NULL and place a Tcl list into the given <i>objPtrRef</i>. Tcl will take that list and first increment its reference count before using it. On completion of that use, Tcl will decrement its reference count. Hence if the list should be disposed of by Tcl when done, it should have a reference count of zero, and if the list should not be disposed of, the filesystem should ensure it returns an object with a reference count of at least one.
<h3>Fileattrsgetproc</h3>Function to process a <b>Tcl_FSFileAttrsGet</b> call, used by <b>file attributes</b>. 

<dl COMPACT><dd><pre>typedef int Tcl_FSFileAttrsGetProc(
 Tcl_Interp *<i>interp</i>,
 int <i>index</i>,
 Tcl_Obj *<i>pathPtr</i>,
 Tcl_Obj **<i>objPtrRef</i>);</pre></dl>
 

 Returns a standard Tcl return code. The attribute value retrieved, which corresponds to the <i>index</i>'th element in the list returned by the <b>Tcl_FSFileAttrStringsProc</b>, is a Tcl_Obj placed in <i>objPtrRef</i> (if <b>TCL_OK</b> was returned) and is likely to have a reference count of zero. Either way we must either store it somewhere (e.g. the Tcl result), or Incr/Decr its reference count to ensure it is properly freed.
<h3>Fileattrssetproc</h3>Function to process a <b>Tcl_FSFileAttrsSet</b> call, used by <b>file attributes</b>. If the filesystem is read-only, there is no need to implement this. 

<dl COMPACT><dd><pre>typedef int Tcl_FSFileAttrsSetProc(
 Tcl_Interp *<i>interp</i>,
 int <i>index</i>,
 Tcl_Obj *<i>pathPtr</i>,
 Tcl_Obj *<i>objPtr</i>);</pre></dl>
 

 The attribute value of the <i>index</i>'th element in the list returned by the Tcl_FSFileAttrStringsProc should be set to the <i>objPtr</i> given.
<h3>Createdirectoryproc</h3>Function to process a <b>Tcl_FSCreateDirectory</b> call. Should be implemented unless the FS is read-only. 

<dl COMPACT><dd><pre>typedef int Tcl_FSCreateDirectoryProc(
 Tcl_Obj *<i>pathPtr</i>);</pre></dl>
 

 The return value is a standard Tcl result indicating whether an error occurred in the process. If successful, a new directory should have been added to the filesystem in the location specified by <i>pathPtr</i>.
<h3>Removedirectoryproc</h3>Function to process a <b>Tcl_FSRemoveDirectory</b> call. Should be implemented unless the FS is read-only. 

<dl COMPACT><dd><pre>typedef int Tcl_FSRemoveDirectoryProc(
 Tcl_Obj *<i>pathPtr</i>,
 int <i>recursive</i>,
 Tcl_Obj **<i>errorPtr</i>);</pre></dl>
 

 The return value is a standard Tcl result indicating whether an error occurred in the process. If successful, the directory specified by <i>pathPtr</i> should have been removed from the filesystem. If the <i>recursive</i> flag is given, then a non-empty directory should be deleted without error. If this flag is not given, then and the directory is non-empty a POSIX ``EEXIST'' error should be signaled. If an error does occur, the name of the file or directory which caused the error should be placed in <i>errorPtr</i>.
<h3>Deletefileproc</h3>Function to process a <b>Tcl_FSDeleteFile</b> call. Should be implemented unless the FS is read-only. 

<dl COMPACT><dd><pre>typedef int Tcl_FSDeleteFileProc(
 Tcl_Obj *<i>pathPtr</i>);</pre></dl>
 

 The return value is a standard Tcl result indicating whether an error occurred in the process. If successful, the file specified by <i>pathPtr</i> should have been removed from the filesystem. Note that, if the filesystem supports symbolic links, Tcl will always call this function and not Tcl_FSRemoveDirectoryProc when needed to delete them (even if they are symbolic links to directories).
<h2>Filesystem Efficiency</h2>These functions need not be implemented for a particular filesystem because the core has a fallback implementation available. See each individual description for the consequences of leaving the field NULL.
<h3>Lstatproc</h3>Function to process a <b>Tcl_FSLstat</b> call. If not implemented, Tcl will attempt to use the <i>statProc</i> defined above instead. Therefore it need only be implemented if a filesystem can differentiate between <b>stat</b> and <b>lstat</b> calls. 

<dl COMPACT><dd><pre>typedef int Tcl_FSLstatProc(
 Tcl_Obj *<i>pathPtr</i>,
 Tcl_StatBuf *<i>statPtr</i>);</pre></dl>
 

 The behavior of this function is very similar to that of the <b>Tcl_FSStatProc</b> defined above, except that if it is applied to a symbolic link, it returns information about the link, not about the target file.
<h3>Copyfileproc</h3>Function to process a <b>Tcl_FSCopyFile</b> call. If not implemented Tcl will fall back on <b>open</b>-r, <b>open</b>-w and <b>fcopy</b> as a copying mechanism. Therefore it need only be implemented if the filesystem can perform that action more efficiently. 

<dl COMPACT><dd><pre>typedef int Tcl_FSCopyFileProc(
 Tcl_Obj *<i>srcPathPtr</i>,
 Tcl_Obj *<i>destPathPtr</i>);</pre></dl>
 

 The return value is a standard Tcl result indicating whether an error occurred in the copying process. Note that, <i>destPathPtr</i> is the name of the file which should become the copy of <i>srcPathPtr</i>. It is never the name of a directory into which <i>srcPathPtr</i> could be copied (i.e. the function is much simpler than the Tcl level <b>file copy</b> subcommand). Note that, if the filesystem supports symbolic links, Tcl will always call this function and not <i>copyDirectoryProc</i> when needed to copy them (even if they are symbolic links to directories). Finally, if the filesystem determines it cannot support the <b>file copy</b> action, calling <b>Tcl_SetErrno(EXDEV)</b> and returning a non-<b>TCL_OK</b> result will tell Tcl to use its standard fallback mechanisms.
<h3>Renamefileproc</h3>Function to process a <b>Tcl_FSRenameFile</b> call. If not implemented, Tcl will fall back on a copy and delete mechanism. Therefore it need only be implemented if the filesystem can perform that action more efficiently. 

<dl COMPACT><dd><pre>typedef int Tcl_FSRenameFileProc(
 Tcl_Obj *<i>srcPathPtr</i>,
 Tcl_Obj *<i>destPathPtr</i>);</pre></dl>
 

 The return value is a standard Tcl result indicating whether an error occurred in the renaming process. If the filesystem determines it cannot support the <b>file rename</b> action, calling <b>Tcl_SetErrno(EXDEV)</b> and returning a non-<b>TCL_OK</b> result will tell Tcl to use its standard fallback mechanisms.
<h3>Copydirectoryproc</h3>Function to process a <b>Tcl_FSCopyDirectory</b> call. If not implemented, Tcl will fall back on a recursive <b>file mkdir</b>, <b>file copy</b> mechanism. Therefore it need only be implemented if the filesystem can perform that action more efficiently. 

<dl COMPACT><dd><pre>typedef int Tcl_FSCopyDirectoryProc(
 Tcl_Obj *<i>srcPathPtr</i>,
 Tcl_Obj *<i>destPathPtr</i>,
 Tcl_Obj **<i>errorPtr</i>);</pre></dl>
 

 The return value is a standard Tcl result indicating whether an error occurred in the copying process. If an error does occur, the name of the file or directory which caused the error should be placed in <i>errorPtr</i>. Note that, <i>destPathPtr</i> is the name of the directory-name which should become the mirror-image of <i>srcPathPtr</i>. It is not the name of a directory into which <i>srcPathPtr</i> should be copied (i.e. the function is much simpler than the Tcl level <b>file copy</b> subcommand). Finally, if the filesystem determines it cannot support the directory copy action, calling <b>Tcl_SetErrno(EXDEV)</b> and returning a non-<b>TCL_OK</b> result will tell Tcl to use its standard fallback mechanisms.
<h3>Loadfileproc</h3>Function to process a <b>Tcl_FSLoadFile</b> call. If not implemented, Tcl will fall back on a copy to native-temp followed by a <b>Tcl_FSLoadFile</b> on that temporary copy. Therefore it need only be implemented if the filesystem can load code directly, or it can be implemented simply to return <b>TCL_ERROR</b> to disable load functionality in this filesystem entirely. 

<dl COMPACT><dd><pre>typedef int Tcl_FSLoadFileProc(
 Tcl_Interp *<i>interp</i>,
 Tcl_Obj *<i>pathPtr</i>,
 Tcl_LoadHandle *<i>handlePtr</i>,
 Tcl_FSUnloadFileProc *<i>unloadProcPtr</i>);</pre></dl>
 

 Returns a standard Tcl completion code. If an error occurs, an error message is left in the <i>interp</i>'s result. The function dynamically loads a binary code file into memory. On a successful load, the <i>handlePtr</i> should be filled with a token for the dynamically loaded file, and the <i>unloadProcPtr</i> should be filled in with the address of a procedure. The unload procedure will be called with the given <b>Tcl_LoadHandle</b> as its only parameter when Tcl needs to unload the file. For example, for the native filesystem, the <b>Tcl_LoadHandle</b> returned is currently a token which can be used in the private <b>TclpFindSymbol</b> to access functions in the new code. Each filesystem is free to define the <b>Tcl_LoadHandle</b> as it requires. Finally, if the filesystem determines it cannot support the file load action, calling <b>Tcl_SetErrno(EXDEV)</b> and returning a non-<b>TCL_OK</b> result will tell Tcl to use its standard fallback mechanisms.
<h3>Unloadfileproc</h3>Function to unload a previously successfully loaded file. If load was implemented, then this should also be implemented, if there is any cleanup action required. 

<dl COMPACT><dd><pre>typedef void Tcl_FSUnloadFileProc(
 Tcl_LoadHandle <i>loadHandle</i>);</pre></dl><h3>Getcwdproc</h3>Function to process a <b>Tcl_FSGetCwd</b> call. Most filesystems need not implement this. It will usually only be called once, if <b>getcwd</b> is called before <b>chdir</b>. May be NULL. 

<dl COMPACT><dd><pre>typedef Tcl_Obj* Tcl_FSGetCwdProc(
 Tcl_Interp *<i>interp</i>);</pre></dl>
 

 If the filesystem supports a native notion of a current working directory (which might perhaps change independent of Tcl), this function should return that cwd as the result, or NULL if the current directory could not be determined (e.g. the user does not have appropriate permissions on the cwd directory). If NULL is returned, an error message is left in the <i>interp</i>'s result.
<h3>Chdirproc</h3>Function to process a <b>Tcl_FSChdir</b> call. If filesystems do not implement this, it will be emulated by a series of directory access checks. Otherwise, virtual filesystems which do implement it need only respond with a positive return result if the <i>pathPtr</i> is a valid, accessible directory in their filesystem. They need not remember the result, since that will be automatically remembered for use by <b>Tcl_FSGetCwd</b>. Real filesystems should carry out the correct action (i.e. call the correct system <b>chdir</b> API). 

<dl COMPACT><dd><pre>typedef int Tcl_FSChdirProc(
 Tcl_Obj *<i>pathPtr</i>);</pre></dl>
 

 The <b>Tcl_FSChdirProc</b> changes the applications current working directory to the value specified in <i>pathPtr</i>. The function returns -1 on error or 0 on success.
<h2>See Also</h2><a HREF="/docs/linux/man/n-cd/">cd</a>(n), <a HREF="/docs/linux/man/n-file/">file</a>(n), <a HREF="/docs/linux/man/n-load/">load</a>(n), <a HREF="/docs/linux/man/n-open/">open</a>(n), <a HREF="/docs/linux/man/n-pwd/">pwd</a>(n), <a HREF="/docs/linux/man/n-unload/">unload</a>(n)
<h2>Keywords</h2>stat, access, filesystem, vfs, virtual
