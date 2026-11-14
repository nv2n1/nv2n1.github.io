---
title: "nfstest-test_util(3)"
name: "nfstest-test_util"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nfstest-test_util/"
description: "nfstest.test_util – Test utilities module"
---

<p>nfstest.test_util &#8211; Test utilities module</p>
<h2>Description</h2>
<p>Provides a set of tools for testing either the NFS client or the NFS server, most of the functionality is focused mainly on testing the client. These tools include the following: </p>
<p>&nbsp;<wbr>&#8211; Process command line arguments<br />
&nbsp;<wbr>&#8211; Provide functionality for PASS/FAIL<br />
&nbsp;<wbr>&#8211; Provide test grouping functionality<br />
&nbsp;<wbr>&#8211; Provide multiple client support<br />
&nbsp;<wbr>&#8211; Logging mechanism<br />
&nbsp;<wbr>&#8211; Debug info control<br />
&nbsp;<wbr>&#8211; Mount/Unmount control<br />
&nbsp;<wbr>&#8211; Create files/directories<br />
&nbsp;<wbr>&#8211; Provide mechanism to start a packet trace<br />
&nbsp;<wbr>&#8211; Provide mechanism to simulate a network partition<br />
&nbsp;<wbr>&#8211; Support for pNFS testing </p>
<p> In order to use some of the functionality available, the user id in all the client hosts must have access to run commands as root using the &#8216;sudo&#8217; command without the need for a password, this includes the host where the test is being executed. This is used to run commands like &#8216;mount&#8217; and &#8216;umount&#8217;. Furthermore, the user id must be able to ssh to remote hosts without the need for a password if test requires the use of multiple clients. </p>
<p> Network partition is simulated by the use of &#8216;iptables&#8217;, please be advised that after every test run the iptables is flushed and reset so any rules previously setup will be lost. Currently, there is no mechanism to restore the iptables rules to their original state.</p>
<h2>Classes</h2>
<h3>class TestUtil(nfstest.nfs_util.NFSUtil)</h3>
<pre>TestUtil object
TestUtil() -&gt; New server object
Usage:
 x = TestUtil()
 # Process command line options
 x.scan_options()
 # Start packet trace using tcpdump
 x.trace_start()
 # Mount volume
 x.mount()
 # Create file
 x.create_file()
 # Unmount volume
 x.umount()
 # Stop packet trace
 x.trace_stop()
 # Exit script
 x.exit()
<code>Methods defined here:</code>
---------------------
<code>__del__(self)</code>
Destructor
Gracefully stop the packet trace, cleanup files, unmount volume,
and reset network.
<code>__init__(self, **kwargs)</code>
Constructor
Initialize object's private data.
<dl><dt><dd><dl><dt><code>sid:</code>
<dd>Test script ID [default: '']
This is used to have options targeted for a given ID without
including these options in any other test script.
<dt><code>usage:</code>
<dd>Usage string [default: '']
<dt><code>testnames:</code>
<dd>List of test names [default: []]
When this list is not empty, the --runtest option is enabled and
test scripts should use the run_tests() method to run all the
tests. Test script should have methods named as &lt;testname&gt;_test.
<dt><code>testgroups:</code>
<dd>Dictionary of test groups where the key is the name of the test
group and its value is a dictionary having the following keys:
tests:
A list of tests belonging to this test group
desc:
Description of the test group, this is displayed
in the help if the name of the test group is also
included in testnames
tincl:
Include a comma separated list of tests belonging to
this test group to the description [default: False]
wrap:
Reformat the description so it fits in lines no
more than the width given. The description is not
formatted for a value of zero [default: 72]
</dl></dl><dl><dt><dd>Example:
 x = TestUtil(testnames=['basic', 'lock'])
 # The following methods should exist:
 x.basic_test()
 x.lock_test()
</dl>
<code>abspath(self, filename, dir=None)</code>
Return the absolute path for the given file name.
<code>cleanup(self)</code>
Clean up test environment.
Remove any files created: test files, trace files.
<code>close_files(self)</code>
Close all files opened by open_files().
<code>config(self, msg)</code>
Display config message and terminate test with an exit value of 2.
<code>create_dir(self, dir=None, mode=493)</code>
Create a directory under the given directory with the given mode.
<code>create_file(self, offset=0, size=None, dir=None, mode=None, **kwds)</code>
Create a file starting to write at given offset with total size
of written data given by the size option.
<dl><dt><dd><dl><dt><code>offset:</code>
<dd>File offset where data will be written to [default: 0]
<dt><code>size:</code>
<dd>Total number of bytes to write [default: --filesize option]
<dt><code>dir:</code>
<dd>Create file under this directory
<dt><code>mode:</code>
<dd>File permissions [default: use default OS permissions]
<dt><code>pattern:</code>
<dd>Data pattern to write to the file [default: data_pattern default]
<dt><code>ftype:</code>
<dd>File type to create [default: FTYPE_FILE]
<dt><code>hole_list:</code>
<dd>List of offsets where each hole is located [default: None]
<dt><code>hole_size:</code>
<dd>Size of each hole [default: --wsize option]
</dl></dl><dl><dt><dd>Returns the file name created, the file name is also stored
in the object attribute filename -- attribute absfile is also
available as the absolute path of the file just created.
File created is removed at cleanup.
</dl>
<code>data_pattern(self, offset, size, pattern=None)</code>
Return data pattern.
<dl><dt><dd><dl><dt><code>offset:</code>
<dd>Starting offset of pattern
<dt><code>size:</code>
<dd>Size of data to return
<dt><code>pattern:</code>
<dd>Data pattern to return, default is of the form:
hex_offset(0x%08X) abcdefghijklmnopqrst</dl></dl>
<code>delay_io(self, delay=None)</code>
Delay I/O by value given or the value given in --iodelay option.
<code>exit(self)</code>
Terminate script with an exit value of 0 when all tests passed
and a value of 1 when there is at least one test failure.
<code>get_dirname(self, dir=None)</code>
Return a unique directory name under the given directory.
<code>get_filename(self, dir=None)</code>
Return a unique file name under the given directory.
<code>get_logname(self)</code>
Get next log file name.
<code>get_name(self)</code>
Get unique name for this instance.
<code>lock_files(self, lock_type=None, offset=0, length=0)</code>
Lock all files opened by open_files().
<code>open_files(self, mode, create=True)</code>
Open files according to given mode, the file descriptors are saved
internally to be used with write_files(), read_files() and
close_files(). The number of files to open is controlled by
the command line option '--nfiles'.
The mode could be either 'r' or 'w' for opening files for reading
or writing respectively. The open flags for mode 'r' is O_RDONLY
while for mode 'w' is O_WRONLY|O_CREAT|O_SYNC. The O_SYNC is used
to avoid the client buffering the written data.
<code>read_files(self)</code>
Read a block of data (size given by --rsize) from all files opened
by open_files() for reading.
<code>run_tests(self, **kwargs)</code>
Run all test specified by the --runtest option.
<dl><dt><dd><dl><dt><code>testnames:</code>
<dd>List of testnames to run [default: all tests given by --testnames]
</dl></dl><dl><dt><dd>All other arguments given are passed to the test methods.
</dl>
<code>scan_options(self)</code>
Process command line options.
Process all the options in the file given by '--file', then the
ones in the command line. This allows for command line options
to over write options given in the file.
Format of options file:
 # For options expecting a value
 &lt;option_name&gt; = &lt;value&gt;
 # For boolean (flag) options
 &lt;option_name&gt;
Process options files and make sure not to process the same file
twice, this is used for the case where HOMECFG and CWDCFG are the
same, more specifically when environment variable HOME is not
defined. Also, the precedence order is defined as follows:
 1. options given in command line
 2. options given in file specified by the -f|--file option
 3. options given in file specified by ./.nfstest
 4. options given in file specified by $HOME/.nfstest
 5. options given in file specified by /etc/nfstest
NOTE:
 Must use the long name of the option (--&lt;option_name&gt;) in the file.
<code>setup(self, nfiles=None)</code>
Set up test environment.
Create nfiles number of files [default: --nfiles option]
<code>test(self, expr, msg, subtest=None, failmsg=None, terminate=False)</code>
Test expr and display message as PASS/FAIL, terminate execution
if terminate option is True.
<dl><dt><dd><dl><dt><code>expr:</code>
<dd>If expr is true, display as a PASS message,
otherwise as a FAIL message
<dt><code>msg:</code>
<dd>Message to display
<dt><code>subtest:</code>
<dd>If given, append this string to the displayed message and
mark this test as a member of the sub-group given by msg
<dt><code>failmsg:</code>
<dd>If given, append this string to the displayed message when
expr is false [default: None]
<dt><code>terminate:</code>
<dd>Terminate execution if true and expr is false [default: False]
</dl></dl><dl><dt><dd>If tverbose=normal or level 1:
 Sub-group message is displayed as a PASS/FAIL message including
 the number of tests that passed and failed within the sub-group
If tverbose=verbose or level 2:
 All tests messages are displayed
</dl>
<code>test_group(self, msg)</code>
Display heading message and start a test group.
If tverbose=group or level 0:
 Group message is displayed as a PASS/FAIL message including the
 number of tests that passed and failed within this test group.
If tverbose=normal|verbose or level 1|2:
 Group message is displayed as a heading messages for the tests
 belonging to this test group.
<code>test_info(self, msg)</code>
Display info message.
<code>test_options(self, name=None)</code>
Get options for the given test name. If the test name is not given
it is determined by inspecting the stack to find which method is
calling this method.
<code>testid_count(self, tid)</code>
Return the number of instances the testid has occurred.
<code>warning(self, msg)</code>
Display warning message.
<code>write_data(self, fd, offset=0, size=None, pattern=None)</code>
Write data to the file given by the file descriptor
<dl><dt><dd><dl><dt><code>fd:</code>
<dd>File descriptor
<dt><code>offset:</code>
<dd>File offset where data will be written to [default: 0]
<dt><code>size:</code>
<dd>Total number of bytes to write [default: --filesize option]
<dt><code>pattern:</code>
<dd>Data pattern to write to the file [default: data_pattern default]
</dl></dl>
<code>write_files(self)</code>
Write a block of data (size given by --wsize) to all files opened
by open_files() for writing.
<code>Static methods defined here:</code>
----------------------------
<code>get_list(value, hash, type=&lt;type 'str'&gt;)</code>
Return a list of elements from the comma separated string.
Validate and translate these elements using the input dictionary
	'hash' where every element in the string is the key of 'hash'
and its value is appended to the returned list.
<code>str_list(value, type=&lt;type 'str'&gt;, sep=',')</code>
Return a list of &lt;type&gt; elements from the comma separated string.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-nfstest-host/">nfstest.host</a>(3),</code> <code><a href="/docs/linux/man/3-nfstest-nfs_util/">nfstest.nfs_util</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
