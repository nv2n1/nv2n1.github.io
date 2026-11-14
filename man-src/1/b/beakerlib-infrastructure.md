---
title: "beakerlib-infrastructure(1)"
name: "beakerlib-infrastructure"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-infrastructure/"
---

<h2 class="name">NAME</h2>
 

 BeakerLib - infrastructure - mounting, backup and service helpers 

<h2>DESCRIPTION</h2>

 BeakerLib functions providing checking and mounting <font SIZE="-1">NFS</font> shares, backing up and restoring files and controlling running services.

<h2>FUNCTIONS</h2>

<h3>Mounting</h3>

 <i>rlMount</i> 

 Create mount point (if neccessary) and mount a <font SIZE="-1">NFS</font> share. 

 <pre>
    rlMount [-o MOUNT_OPTS] server share mountpoint
</pre>
<dl>
<dt>server
<dd> <font SIZE="-1">NFS</font> server hostname.
<dt>share
<dd> Shared directory name.
<dt>mountpoint
<dd> Local mount point.
<dt><font SIZE="-1">MOUNT_OPTS</font>
<dd> Mount options.</dl>
 

 Returns 0 if mounting the share was successful. 

 <i>rlCheckMount</i> 

 Check either if a directory is a mountpoint, if it is a mountpoint to a specific server, or if it is a mountpoint to a specific export on a specific server and if it uses specific mount options. 

 <pre><code>
rlCheckMount[-o MOUNT_OPTS] mountpoint
    rlCheckMount[-o MOUNT_OPTS] server mountpoint
        rlCheckMount[-o MOUNT_OPTS] server share mountpoint
</code></pre>
<dl>
<dt>mountpoint
<dd> Local mount point.
<dt>server
<dd> <font SIZE="-1">NFS</font> server hostname
<dt>share
<dd> Shared directory name
<dt><font SIZE="-1">MOUNT_OPTS</font>
<dd> Mount options to check (comma separated list)</dl>
 

 With one parameter, returns 0 when specified directory exists and is a mountpoint. With two parameters, returns 0 when specific directory exists, is a mountpoint and an export from specific server is mounted there. With three parameters, returns 0 if a specific shared directory is mounted on a given server on a given mountpoint 

 If the -o option is provided, returns 0 if the mountpoint uses all the given options, 2 otherwise. 

 <i>rlAssertMount</i> 

 Assertion making sure that given directory is a mount point, if it is a mountpoint to a specific server, or if it is a mountpoint to a specific export on a specific server and if it uses specific mount options. 

 
rlAssertMount[-o MOUNT_OPTS] mountpoint
    rlAssertMount[-o MOUNT_OPTS] server mountpoint
        rlAssertMount[-o MOUNT_OPTS] server share mountpoint

<dl>
<dt>mountpoint
<dd> Local mount point.
<dt>server
<dd> <font SIZE="-1">NFS</font> server hostname
<dt>share
<dd> Shared directory name
<dt><font SIZE="-1">MOUNT_OPTS</font>
<dd> Mount options to check (comma separated list)</dl>
 

 With one parameter, returns 0 when specified directory exists and is a mountpoint. With two parameters, returns 0 when specific directory exists, is a mountpoint and an export from specific server is mounted there. With three parameters, returns 0 if a specific shared directory is mounted on a given server on a given mountpoint. Asserts <font SIZE="-1">PASS</font> when the condition is true. 

 If the -o option is provided, asserts <font SIZE="-1">PASS</font> if the above conditions are met and the mountpoint uses all the given options. 

 <i>rlHash, rlUnhash</i> 

 Hashes/Unhashes given string. 

 
rlHash[--decode][--algorithm HASH_ALG]-- stdin | STRING rlUnhash[--algorithm HASH_ALG]-- stdin | STRING

<dl>
<dt>--decode
<dd> Unhash given string.
<dt>--algorithm
<dd> Use given hash algorithm. Currently supported algorithms: 
&nbsp;<wbr>&nbsp;<wbr>base64 
&nbsp;<wbr>&nbsp;<wbr>base64_&nbsp;<wbr>- this is standard base64 where&nbsp;<wbr>'='&nbsp;<wbr>is replaced by&nbsp;<wbr>'_' 
&nbsp;<wbr>&nbsp;<wbr>hex 

 Defaults to hex. Default algorithm can be override using global variable rlHashAlgorithm.
<dt>--stdin
<dd> Get the string from stdin.
<dt><font SIZE="-1">STRING</font>
<dd> String to be hashed/unhashed.</dl>
 

 Returns 0 if success. 

 Example with --clean: 

 <pre>
    hash=rlHash &quot;text&quot;
</pre>

<h3>Backup and Restore</h3>

 <i>rlFileBackup</i> 

 Create a backup of files or directories (recursive). Can be used multiple times to add more files to backup. Backing up an already backed up file overwrites the original backup. 

 <pre><code>
rlFileBackup[--clean][--namespace name][--missing - ok | --no - missing - ok] file[file...]
</code></pre> 

 You can use <tt>&quot;rlRun&quot;</tt> for asserting the result but keep in mind meaning of exit codes, especialy exit code 8, if using without --clean option.
<dl>
<dt>--clean
<dd> If this option is provided (have to be first option of the command), then file/dir backuped using this command (provided in next options) will be (recursively) removed before we will restore it. This option implies --missing-ok, this can be overridden by --no-missing-ok.
<dt>--namespace name
<dd> Specifies the namespace to use. Namespaces can be used to separate backups and their restoration.
<dt>--missing-ok
<dd> Do not raise an error in case of missing file to backup.
<dt>--no-missing-ok
<dd> Do raise an error in case of missing file to backup. This is useful with --clean. This behaviour can be globally set by global variable BEAKERLIB_FILEBACKUP_MISSING_OK=false.
<dt>file
<dd> Files and/or directories to be backed up.</dl>
 

 Returns 0 if the backup was successful. Returns 1 if parsing of parameters was not successful. Returns 2 if no files specification was provided. Returns 3 if <font SIZE="-1">BEAKERLIB_DIR</font> variable is not set, e.g. rlJournalStart was not executed. Returns 4 if creating of main backup destination directories was not successful. Returns 5 if creating of file specific backup destination directories was not successful. Returns 6 if the copy of backed up files was not successful. Returns 7 if attributes of backedup files were not successfuly copied. Returns 8 if backed up files does not exist. This can be suppressed based on other options. 

 Example with --clean: 

 <pre>
    touch cleandir/aaa
    rlRun &quot;rlFileBackup --clean cleandir/&quot;
    touch cleandir/bbb
    ls cleandir/
    aaa   bbb
    rlRun &quot;rlFileRestore&quot;
    ls cleandir/
    aaa
</pre> 

 <i>rlFileRestore</i> 

 Restore backed up files to their original location. <tt>&quot;rlFileRestore&quot;</tt> does not remove new files appearing after backup has been made. If you don't want to leave anything behind just remove the whole original tree before running <tt>&quot;rlFileRestore&quot;</tt>, or see <tt>&quot;--clean&quot;</tt> option of <tt>&quot;rlFileBackup&quot;</tt>. 

 <pre>
    rlFileRestore [--namespace name]
</pre> 

 You can use <tt>&quot;rlRun&quot;</tt> for asserting the result.
<dl>
<dt>--namespace name
<dd> Specifies the namespace to use. Namespaces can be used to separate backups and their restoration.</dl>
 

 Returns 0 if backup dir is found and files are restored successfully. 

 Return code bits meaning <font SIZE="-1">XXXXX 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>||||| 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>||||\_&nbsp;<wbr>error parsing parameters 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|||\__&nbsp;<wbr>could not find backup directory 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>||\___&nbsp;<wbr>files cleanup failed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|\____&nbsp;<wbr>files restore failed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\_____&nbsp;<wbr>no files were restored nor cleaned

<h3>Services</h3>

 Following routines implement comfortable way how to start/stop system services with the possibility to restore them to their original state after testing. 

 <i>rlServiceStart</i> 

 Make sure the given <tt>&quot;service&quot;</tt> is running with fresh configuration. (Start it if it is stopped and restart if it is already running.) In addition, when called for the first time, the current state is saved so that the <tt>&quot;service&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlServiceRestore&quot;</tt>. 

 <pre>
    rlServiceStart service [service...]
</pre>
<dl>
<dt>service
<dd> Name of the service(s) to start.</dl>
 

 Returns number of services which failed to start/restart; thus zero is returned when everything is <font SIZE="-1">OK.</font> 

 <i>rlServiceStop</i> 

 Make sure the given <tt>&quot;service&quot;</tt> is stopped. Stop it if it is running and do nothing when it is already stopped. In addition, when called for the first time, the current state is saved so that the <tt>&quot;service&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlServiceRestore&quot;</tt>. 

 <pre>
    rlServiceStop service [service...]
</pre>
<dl>
<dt>service
<dd> Name of the service(s) to stop.</dl>
 

 Returns number of services which failed to become stopped; thus zero is returned when everything is <font SIZE="-1">OK.</font> 

 <i>rlServiceRestore</i> 

 Restore given <tt>&quot;service&quot;</tt> into its original state (before the first <tt>&quot;rlServiceStart&quot;</tt> or <tt>&quot;rlServiceStop&quot;</tt> was called). 

 <pre>
    rlServiceRestore [service...]
</pre>
<dl>
<dt>service
<dd> Name of the service(s) to restore to original state. All services will be restored in reverse order if no service name is given.</dl>
 

 Returns number of services which failed to get back to their original state; thus zero is returned when everything is <font SIZE="-1">OK.</font> 

 <i>rlServiceEnable</i> 

 Enables selected services if needed, or does nothing if already enabled. In addition, when called for the first time, the current state is saved so that the <tt>&quot;service&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlServiceRestore&quot;</tt>. 

 <pre>
    rlServiceEnable service [service...]
</pre>
<dl>
<dt>service
<dd> Name of the service(s) to enable.</dl>
 

 Returns number of services which failed enablement; thus zero is returned when everything is <font SIZE="-1">OK.</font> 

 <i>rlServiceDisable</i> 

 Disables selected services if needed, or does nothing if already disabled. In addition, when called for the first time, the current state is saved so that the <tt>&quot;service&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlServiceRestore&quot;</tt>. 

 <pre>
    rlServiceDisable service [service...]
</pre>
<dl>
<dt>service
<dd> Name of the service(s) to disable.</dl>
 

 Returns number of services which failed disablement; thus zero is returned when everything is <font SIZE="-1">OK.</font>

<h3>Sockets</h3>

 Following routines implement comfortable way how to start/stop system sockets with the possibility to restore them to their original state after testing. 

 <i>rlSocketStart</i> 

 Make sure the given <tt>&quot;socket&quot;</tt> is running. (Start it if stopped, leave it if already running.) In addition, when called for the first time, the current state is saved so that the <tt>&quot;socket&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlSocketRestore&quot;</tt>. 

 <pre>
    rlSocketStart socket [socket...]
</pre>
<dl>
<dt>socket
<dd> Name of the socket(s) to start.</dl>
 

 Returns number of sockets which failed to start/restart; thus zero is returned when everything is <font SIZE="-1">OK.</font> 

 <i>rlSocketStop</i> 

 Make sure the given <tt>&quot;socket&quot;</tt> is stopped. Stop it if it is running and do nothing when it is already stopped. In addition, when called for the first time, the current state is saved so that the <tt>&quot;socket&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlSocketRestore&quot;</tt>. 

 <pre>
    rlSocketStop socket [socket...]
</pre>
<dl>
<dt>socket
<dd> Name of the socket(s) to stop.</dl>
 

 Returns number of sockets which failed to become stopped; thus zero is returned when everything is <font SIZE="-1">OK.</font> 

 <i>rlSocketRestore</i> 

 Restore given <tt>&quot;socket&quot;</tt> into its original state (before the first <tt>&quot;rlSocketStart&quot;</tt> or <tt>&quot;rlSocketStop&quot;</tt> was called). 

 Warning !!! Xinetd process [even though it might have been used] is <font SIZE="-1">NOT</font> restored. It is recommended to call rlServiceRestore xinetd as well. 

 <pre>
    rlSocketRestore socket [socket...]
</pre>
<dl>
<dt>socket
<dd> Name of the socket(s) to restore to original state.</dl>
 

 Returns number of sockets which failed to get back to their original state; thus zero is returned when everything is <font SIZE="-1">OK.</font>

<h3>Cleanup management</h3>

 Cleanup management works with a so-called cleanup buffer, which is a temporary representation of what should be run at cleanup time, and a final cleanup script (executable), which is generated from this buffer and wraps it using BeakerLib essentials (journal initialization, cleanup phase, ...). The cleanup script must always be updated on an atomic basis (filesystem-wise) to allow an asynchronous execution by a third party (ie. test watcher). 

 The test watcher usage is mandatory for the cleanup management system to work properly as it is the test watcher that executes the actual cleanup script. Limited, catastrophe-avoiding mechanism is in place even when the test is not run in test watcher, but that should be seen as a backup and such situation is to be avoided whenever possible. 

 The cleanup script shares all environment (variables, exported or not, and functions) with the test itself - the cleanup append/prepend functions ``sample'' or ``snapshot'' the environment at the time of their call, <font SIZE="-1">IOW</font> any changes to the test environment are synchronized to the cleanup script only upon calling append/prepend. When the append/prepend functions are called within a function which has local variables, these will appear as global in the cleanup. 

 While the cleanup script receives <tt>$PWD</tt> from the test, its working dir is set to the initial test execution dir even if <tt>$PWD</tt> contains something else. It is impossible to use relative paths inside cleanup reliably - certain parts of the cleanup might have been added under different current directories (CWDs). Therefore always use absolute paths in append/prepend cleanup or make sure you never 'cd' elsewhere (ie. to a TmpDir). 

 <i>rlCleanupAppend</i> 

 Appends a string to the cleanup buffer and recreates the cleanup script. 

 <pre>
    rlCleanupAppend string
</pre> 

 Returns 0 if the operation was successful, 1 otherwise. 

 <i>rlCleanupPrepend</i> 

 Prepends a string to the cleanup buffer and recreates the cleanup script. 

 <pre>
    rlCleanupPrepend string
</pre> 

 Returns 0 if the operation was successful, 1 otherwise.

<h2>AUTHORS</h2>

<dl>
<dt>&bull;
<dd> Petr Muller &lt;pmuller [at] redhat.com&gt;
<dt>&bull;
<dd> Jan Hutar &lt;jhutar [at] redhat.com&gt;
<dt>&bull;
<dd> Petr Splichal &lt;psplicha [at] redhat.com&gt;
<dt>&bull;
<dd> Ales Zelinka &lt;azelinka [at] redhat.com&gt;
<dt>&bull;
<dd> Karel Srot &lt;ksrot [at] redhat.com&gt; 

</dl>

<h2>Index</h2>


