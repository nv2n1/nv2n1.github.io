---
title: "gearmand(8)"
name: "gearmand"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gearmand/"
description: "gearmand – Gearmand Documentation, http://gearman.info/"
---

<p>gearmand &#8211; Gearmand Documentation, <a rel="nofollow" href="http://gearman.info/">http://gearman.info/</a></p>
<h2>Synopsis</h2>
<p><code>General options</code></p>
<dl>
<dt><code>-b [ &#8211;backlog ] arg (=32)</code></p>
<dd>Number of backlog connections for listen.</p>
<dt><code>&#8211;check-args</code></p>
<dd>Check command line and configuration file argments and then exit.</p>
<dt><code>-d [ &#8211;daemon ]</code></p>
<dd>Daemon, detach and run in the background.</p>
<dt><code>-f [ &#8211;file-descriptors ] arg</code></p>
<dd>Number of file descriptors to allow for the process (total connections will be slightly less). Default is max allowed for user.</p>
<dt><code>-h [ &#8211;help ]</code></p>
<dd>Print this help menu.</p>
<dt><code>-j [ &#8211;job-retries ] arg (=0)</code></p>
<dd>Number of attempts to run the job before the job server removes it. This is helpful to ensure a bad job does not crash all available workers. Default is no limit.</p>
<dt><code>-l [ &#8211;log-file ] arg</code></p>
<dd>Log file to write errors and information to. Turning this option on also forces the first verbose level to be enabled.</p>
<dt><code>-L [ &#8211;listen ] arg</code></p>
<dd>Address the server should listen on. Default is INADDR_ANY.</p>
<dt><code>-p [ &#8211;port ] arg (=4730)</code></p>
<dd>Port the server should listen on.</p>
<dt><code>-P [ &#8211;pid-file ] arg</code></p>
<dd>File to write process ID out to.</p>
<dt><code>-r [ &#8211;protocol ] arg</code></p>
<dd>Load protocol module.</p>
<dt><code>-R [ &#8211;round-robin ]</code></p>
<dd>Assign work in round-robin order per worker connection. The default is to assign work in the order of functions added by the worker.</p>
<dt><code>-q [ &#8211;queue-type ] arg</code></p>
<dd>Persistent queue type to use.</p>
<dt><code>-t [ &#8211;threads ] arg (=4)</code></p>
<dd>Number of I/O threads to use. Default=4.</p>
<dt><code>-u [ &#8211;user ] arg</code></p>
<dd>Switch to given user after startup.</p>
<dt><code>-v [ &#8211;verbose ] arg (=v)</code></p>
<dd>Increase verbosity level by one.</p>
<dt><code>-V [ &#8211;version ]</code></p>
<dd>Display the version of gearmand and exit.</p>
<dt><code>-w [ &#8211;worker-wakeup ] arg (=0)</code></p>
<dd>Number of workers to wakeup for each job received. The default is to wakeup all available workers.</p>
<dt><code>&#8211;keepalive</code></p>
<dd>Enable keepalive on sockets.</p>
<dt><code>&#8211;keepalive-idle arg (=-1)</code></p>
<dd>If keepalive is enabled, set the value for TCP_KEEPIDLE for systems that support it. A value of -1 means that either the system does not support it or an error occurred when trying to retrieve the default value.</p>
<dt><code>&#8211;keepalive-interval arg (=-1)</code></p>
<dd>If keepalive is enabled, set the value for TCP_KEEPINTVL for systems that support it. A value of -1 means that either the system does not support it or an error occurred when trying to retrieve the default value.</p>
<dt><code>&#8211;keepalive-count arg (=-1)</code></p>
<dd>If keepalive is enabled, set the value for TCP_KEEPCNT for systems that support it. A value of -1 means that either the system does not support it or an error occurred when trying to retrieve the default value. </p>
<p> <code>HTTP:</code></p>
<dt><code>&#8211;http-port arg (=8080)</code></p>
<dd>Port to listen on. </p>
<p> <code>sqlite</code></p>
<dt><code>&#8211;libsqlite3-db arg</code></p>
<dd>Database file to use.</p>
<dt><code>&#8211;libsqlite3-table arg (=gearman_queue)</code></p>
<dd>Table to use. </p>
<p> <code>Memcached(libmemcached)</code></p>
<dt><code>&#8211;libmemcached-servers arg</code></p>
<dd>List of Memcached servers to use. </p>
<p> <code>Drizzle/MySQL(libdrizzle)</code></p>
<dt><code>&#8211;libdrizzle-host arg</code></p>
<dd>Host of server.</p>
<dt><code>&#8211;libdrizzle-port arg</code></p>
<dd>Port of server. (by default Drizzle)</p>
<dt><code>&#8211;libdrizzle-uds arg</code></p>
<dd>Unix domain socket for server.</p>
<dt><code>&#8211;libdrizzle-user arg</code></p>
<dd>User name for authentication.</p>
<dt><code>&#8211;libdrizzle-password arg</code></p>
<dd>Password for authentication.</p>
<dt><code>&#8211;libdrizzle-db arg</code></p>
<dd>Schema/Database to use.</p>
<dt><code>&#8211;libdrizzle-table arg</code></p>
<dd>Table to use.</p>
<dt><code>&#8211;libdrizzle-mysql arg</code></p>
<dd>Use MySQL protocol. </p>
<p> <code>Postgres</code></p>
<dt><code>&#8211;libpq-conninfo arg</code></p>
<dd>PostgreSQL connection information string.</p>
<dt><code>&#8211;libpq-table arg (=queue)</code></p>
<dd>Table to use. </p>
<p> <code>tokyocabinet</code></p>
<dt><code>&#8211;libtokyocabinet-file arg</code></p>
<dd>File name of the database. [see: man tcadb, tcadbopen() for name guidelines]</p>
<dt><code>&#8211;libtokyocabinet-optimize</code></p>
<dd>Optimize database on open. [default=true]</dl>
<h2>Description</h2>
<p>Gearman provides a generic application framework to farm out work to other machines or processes that are better suited to do the work. It allows you to do work in parallel, to load balance processing, and to call functions between languages. It can be used in a variety of applications, from high-availability web sites to the transport of database replication events. In other words, it is the nervous system for how distributed processing communicates. A few strong points about Gearman:</p>
<dl>
<dt>&bull;</p>
<dd>Open Source &#8211; It&#8217;s free! (in both meanings of the word) Gearman has an active open source community that is easy to get involved with if you need help or want to contribute.</p>
<dt>&bull;</p>
<dd>Multi-language &#8211; There are interfaces for a number of languages, and this list is growing. You also have the option to write heterogeneous applications with clients submitting work in one language and workers performing that work in another.</p>
<dt>&bull;</p>
<dd>Flexible &#8211; You are not tied to any specific design pattern. You can quickly put together distributed applications using any model you choose, one of those options being Map/Reduce.</p>
<dt>&bull;</p>
<dd>Fast &#8211; Gearman has a simple protocol and interface with a new optimized server in C to minimize your application overhead.</p>
<dt>&bull;</p>
<dd>Embeddable &#8211; Since Gearman is fast and lightweight, it is great for applications of all sizes. It is also easy to introduce into existing applications with minimal overhead.</p>
<dt>&bull;</p>
<dd>No single point of failure &#8211; Gearman can not only help scale systems, but can do it in a fault tolerant way.</dl>
<h3>Thread Model</h3>
<p>The -t option to gearmand allows you to specify multiple I/O threads, this is enabled by default. There are currently three types of threads in the job server: </p>
<p> Listening and management thread &#8211; only one I/O thread &#8211; can have many Processing thread &#8211; only one </p>
<p> When no -t option is given or -t 0 is given, all of three thread types happen within a single thread. When -t 1 is given, there is a thread for listening/management and a thread for I/O and processing. When -t 2 is given, there is a thread for each type of thread above. For all -t option values above 2, more I/O threads are created. </p>
<p> The listening and management thread is mainly responsible for accepting new connections and assigning those connections to an I/O thread (if there are many). It also coordinates startup and shutdown within the server. This thread will have an instance of libevent for managing socket events and signals on an internal pipe. This pipe is used to wakeup the thread or to coordinate shutdown. </p>
<p> The I/O thread is responsible for doing the read and write system calls on the sockets and initial packet parsing. Once the packet has been parsed it it put into an asynchronous queue for the processing thread (each thread has it&#8217;s own queue so there is very little contention). Each I/O thread has it&#8217;s own instance of libevent for managing socket events and signals on an internal pipe like the listening thread. </p>
<p> The processing thread should have no system calls within it (except for the occasional brk() for more memory), and manages the various lists and hash tables used for tracking unique keys, job handles, functions, and job queues. All packets that need to be sent back to connections are put into an asynchronous queue for the I/O thread. The I/O thread will pick these up and send them back over the connected socket. All packets flow through the processing thread since it contains the information needed to process the packets. This is due to the complex nature of the various lists and hash tables. If multiple threads were modifying them the locking overhead would most likely cause worse performance than having it in a single thread (and would also complicate the code). In the future more work may be pushed to the I/O threads, and the processing thread can retain minimal functionality to manage those tables and lists. So far this has not been a significant bottleneck, a 16 core Intel machine is able to process upwards of 50k jobs per second. </p>
<p> For thread safety to work when UUID are generated, you must be running the uuidd daemon.</p>
<h3>Persistent Queues</h3>
<p>Inside the Gearman job server, all job queues are stored in memory. This means if a server restarts or crashes with pending jobs, they will be lost and are never run by a worker. Persistent queues were added to allow background jobs to be stored in an external durable queue so they may live between server restarts and crashes. The persistent queue is only enabled for background jobs because foreground jobs have an attached client. If a job server goes away, the client can detect this and restart the foreground job somewhere else (or report an error back to the original caller). Background jobs on the other hand have no attached client and are simply expected to be run when submitted. </p>
<p> The persistent queue works by calling a module callback function right before putting a new job in the internal queue for pending jobs to be run. This allows the module to store the job about to be run in some persistent way so that it can later be replayed during a restart. Once it is stored through the module, the job is put onto the active runnable queue, waking up available workers if needed. Once the job has been successfully completed by a worker, another module callback function is called to notify the module the job is done and can be removed. If a job server crashes or is restarted between these two calls for a job, the jobs are reloaded during the next job server start. When the job server starts up, it will call a replay callback function in the module to provide a list of all jobs that were not complete. This is used to populate the internal memory queue of jobs to be run. Once this replay is complete, the job server finishes its initialization and the jobs are now runnable once workers connect (the queue should be in the same state as when it crashed). These jobs are removed from the persistent queue when completed as normal. NOTE: Deleting jobs from the persistent queue storage will not remove them from the in-memory queue while the server is running. </p>
<p> The queues are implemented using a modular interface so it is easy to add new data stores for the persistent queue. </p>
<p> A persistent queue module is enabled by passing the -q or –queue-type option to gearmand. Run gearmand –help to see which queue modules are supported on your system. If you are missing options for one you would like to use, you will need to install any dependencies and then recompile the gearmand package.</p>
<h3>Extended Protocols</h3>
<p>The protocol plugin interface allows you to take over the packet send and receive functions, allowing you to pack the buffers as required by the protocol. The core read and write functions can (and should) be used by the protocol plugin.</p>
<h3>Http</h3>
<p>This protocol plugin allows you to map HTTP requests to Gearman jobs. It only provides client job submission currently, but it may be extended to support other request types in the future. The plugin can handle both GET and POST data, the latter being used to send a workload to the job server. The URL being requested is translated into the function being called. </p>
<p> For example, the request: </p>
<pre>POST /reverse HTTP/1.1
Content-Length: 12
Hello world!</pre>
<p>Is translated into a job submission request for the function “reverse” and workload “Hello world!”. This will respond with: </p>
<pre>HTTP/1.0 200 OK
X-Gearman-Job-Handle: H:lap:4
Content-Length: 12
Server: Gearman/0.8
!dlrow olleH</pre>
<p>The following headers can be passed to change the behavior of the job: </p>
<pre>* X-Gearman-Unique: &lt;unique key&gt;
* X-Gearman-Background: true
* X-Gearman-Priority: &lt;high|low&gt;</pre>
<p>For example, to run a low priority background job, the following request can be sent: </p>
<pre>POST /reverse HTTP/1.1
Content-Length: 12
X-Gearman-Background: true
X-Gearman-Priority: low
Hello world!</pre>
<p>The response for this request will not have any data associated with it since it was a background job: </p>
<pre>HTTP/1.0 200 OK
X-Gearman-Job-Handle: H:lap:6
Content-Length: 0
Server: Gearman/0.8</pre>
<p>The HTTP protocol should be considered experimental.</p>
<h2>Home</h2>
<p>To find out more information please check: <i><a rel="nofollow" href="http://gearman.info/">http://gearman.info/</a></i></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-gearman/">gearman</a>(1)</i> <i><a href="/docs/linux/man/1-gearadmin/">gearadmin</a>(1)</i> <i><a href="/docs/linux/man/3-libgearmand/">libgearmand</a>(3)</i></p>
<h2>Author</h2>
<p>Data Differential <a rel="nofollow" href="http://www.datadifferential.com/">http://www.datadifferential.com/</a></p>
<h2>Copyright</h2>
<p>2011-2013, Data Differential, <a rel="nofollow" href="http://www.datadifferential.com/">http://www.datadifferential.com/</a></p>
