---
title: "nfstest-rexec(3)"
name: "nfstest-rexec"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nfstest-rexec/"
description: "nfstest.rexec – Remote procedure module"
---

<p>nfstest.rexec &#8211; Remote procedure module</p>
<h2>Description</h2>
<p>Provides a set of tools for executing a wide range commands, statements, expressions or functions on a remote host by running a server process on the remote host serving requests without disconnecting. This allows for a sequence of operations to be done remotely and not losing state. A file could be opened remotely, do some other things and then write to the same opened file without opening the file again. </p>
<p> In order to use this module the user id must be able to &#8216;ssh&#8217; to the remote host without the need for a password.</p>
<h2>Classes</h2>
<h3>class Rexec(baseobj.BaseObj)</h3>
<pre>Rexec object
 Rexec() -&gt; New remote procedure object
 Arguments:
 servername:
 Name or IP address of remote server
 logfile:
 Name of logfile to create on remote server
 Usage:
 from nfstest.rexec import Rexec
 # Function to be defined at remote host
 def <a href="//www.systutorials.com/docs/linux/man/n-add_one/">add_one</a>(n):
 return n + 1
 # Function to be defined at remote host
 def get_time(delay=0):
 time.sleep(delay)
 return time.time()
 # Create remote procedure object
 x = Rexec(&quot;192.168.0.85&quot;)
 # Define function at remote host
 x.rcode(add_one)
 # Evaluate the expression calling add_one()
 out = x.reval(&quot;add_one(67)&quot;)
 # Run the function with the given argument
 out = x.run(&quot;add_one&quot;, 7)
 # Run built-in functions
 import time
 out = x.run(time.time)
 # Import libraries and symbols
 x.rimport(&quot;time&quot;, [&quot;sleep&quot;])
 x.run(&quot;sleep&quot;, 2)
 # Define function at remote host -- since function uses the
 # time module, this module must be first imported
 x.rimport(&quot;time&quot;)
 x.rcode(get_time)
 # Evaluate the expression calling get_time()
 out = x.reval(&quot;get_time()&quot;)
 # Run the function with the given argument
 out = x.run(&quot;get_time&quot;, 10)
 # Open file on remote host
 fd = x.run(os.open, &quot;/tmp/testfile&quot;, os.O_WRONLY|os.O_CREAT|os.O_TRUNC)
 count = x.run(os.write, fd, &quot;hello there
	&quot;)
 x.run(os.close, fd)
 # Use of positional arguments
 out = x.run('get_time', 2)
 # Use of named arguments
 out = x.run('get_time', delay=2)
 # Use of NOWAIT option for long running functions so other things
 # can be done while waiting
 x.run('get_time', 2, NOWAIT=True)
 while True:
 # Poll every 0.1 secs to see if function has finished
 if x.poll(0.1):
 # Get results
 out = x.results()
 break
<code>Methods defined here:</code>
---------------------
<code>__del__(self)</code>
Destructor
<code>__init__(self, servername='', logfile=None, sync_timeout=0.10000000000000001)</code>
Constructor
Initialize object's private data.
<dl><dt><dd><dl><dt><code>servername:</code>
<dd>Host name or IP address of host where remote server will run
<dt><code>logfile:</code>
<dd>Pathname of log file to be created on remote host
[Default: &quot;/dev/null&quot;]
<dt><code>sync_timeout:</code>
<dd>Timeout used for synchronizing the connection stream
[Default: 0.1]
</dl></dl>
<code>poll(self, timeout=0)</code>
Return whether there is any data available to be read
<dl><dt><dd><dl><dt><code>timeout:</code>
<dd>Maximum time in seconds to block, if timeout is None then
an infinite timeout is used
</dl></dl>
<code>rcode(self, code)</code>
Define function on remote server
<code>results(self)</code>
Return pending results
<code>reval(self, expr)</code>
Evaluate expression on remote server
<code>rexec(self, expr)</code>
Execute statement on remote server
<code>rimport(self, module, symbols=[])</code>
Import module on remote server
<dl><dt><dd><dl><dt><code>module:</code>
<dd>Module to import in the remote server
<dt><code>symbols:</code>
<dd>If given, import only these symbols from the module
</dl></dl>
<code>run(self, *kwts, **kwds)</code>
Run function on remote server
The first positional argument is the function to be executed.
All other positional arguments and any named arguments are treated
as arguments to the function
<code>wait(self, objlist=None, timeout=0)</code>
Return a list of Rexec objects where data is available to be read
<dl><dt><dd><dl><dt><code>objlist:</code>
<dd>List of Rexec objects to poll, if not given use current object
<dt><code>timeout:</code>
<dd>Maximum time in seconds to block, if timeout is None then
an infinite timeout is used
</dl></dl></pre>
<h2>Functions</h2>
<h3>bare_server(port, logfile)</h3>
<p>Bare-bones remote server</p>
<h3>proc_requests(fd, conn)</h3>
<p>Main remote procedure server </p>
<dl>
<dd>
<dl>
<dt><code>fd:</code></p>
<dd>File descriptor for logfile</p>
<dt><code>conn:</code></p>
<dd>Connection object</dl>
</dl>
<h3>write_log(fd, msg, nl=&#8217;)</h3>
<p>Return timestamp</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
