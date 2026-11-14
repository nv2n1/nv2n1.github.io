---
title: "varnishd(1)"
name: "varnishd"
section: "1"
letter: "v"
url: "/docs/linux/man/1-varnishd/"
description: "varnishd – HTTP accelerator daemon"
---

<h2>NAME</h2>
<p> varnishd &#8211; HTTP accelerator daemon</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>varnishd [-a address[:port]] [-b host[:port]] [-C] [-d] [-f config]</code></p>
<dd> [-F] [-g group] [-h type[,options]] [-i identity] [-l shl[,free[,fill]]] [-M address:port] [-n name] [-P file] [-p param=value] [-r param[,param&#8230;] [-s [name=]kind[,options]] [-S secret-file] [-T address[:port]] [-t ttl] [-u user] [-V]</dl>
<h2>DESCRIPTION</h2>
<p> The varnishd daemon accepts HTTP requests from clients, passes them on to a backend server and caches the returned documents to better satisfy future requests for the same document.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a address[:port][,address[:port][&#8230;]</code></p>
<dd> Listen for client requests on the specified address and port. The address can be a host name (“localhost”), an IPv4 dotted-quad (“127.0.0.1”), or an IPv6 address enclosed in square brackets (“[::1]”). If address is not specified, varnishd will listen on all available IPv4 and IPv6 interfaces. If port is not specified, the default HTTP port as listed in /etc/services is used. Multiple listening addresses and ports can be specified as a whitespace or comma -separated list.</p>
<dt><code>-b host[:port]</code></p>
<dd> Use the specified host as backend server. If port is not specified, the default is 8080.</p>
<dt><code>-C</code></p>
<dd> Print VCL code compiled to C language and exit. Specify the VCL file to compile with the -f option.</p>
<dt><code>-d</code></p>
<dd> Enables debugging mode: The parent process runs in the foreground with a CLI connection on stdin/stdout, and the child process must be started explicitly with a CLI command. Terminating the parent process will also terminate the child.</p>
<dt><code>-f</code><i>&nbsp;<wbr>config</i></p>
<dd> Use the specified VCL configuration file instead of the builtin default. See <a href="/docs/linux/man/7-vcl/">vcl</a>(7) for details on VCL syntax. When no configuration is supplied varnishd will not start the cache process.</p>
<dt><code>-F</code></p>
<dd> Run in the foreground.</p>
<dt><code>-g</code><i>&nbsp;<wbr>group</i></p>
<dd> Specifies the name of an unprivileged group to which the child process should switch before it starts accepting connections. This is a shortcut for specifying the group run-time parameter.</p>
<dt><code>-h type[,options]</code></p>
<dd> Specifies the hash algorithm. See Hash Algorithms for a list of supported algorithms.</p>
<dt><code>-i</code><i>&nbsp;<wbr>identity</i></p>
<dd> Specify the identity of the Varnish server. This can be accessed using server.identity from VCL</p>
<dt><code>-l shl[,free[,fill]]</code></p>
<dd> Specifies size of shmlog file. shl is the store for the shared memory log records [80M], free is the store for other allocations [1M] and fill determines how the log is [+]. Scaling suffixes like &#8216;k&#8217;, &#8216;M&#8217; can be used up to (E)xabytes. Default is 80 Megabytes.</p>
<dt><code>-M address:port</code></p>
<dd> Connect to this port and offer the command line interface. Think of it as a reverse shell. When running with -M and there is no backend defined the child process (the cache) will not start initially.</p>
<dt><code>-n</code><i>&nbsp;<wbr>name</i></p>
<dd> Specify the name for this instance. Amonst other things, this name is used to construct the name of the directory in which varnishd keeps temporary files and persistent state. If the specified name begins with a forward slash, it is interpreted as the absolute path to the directory which should be used for this purpose.</p>
<dt><code>-P</code><i>&nbsp;<wbr>file</i></p>
<dd> Write the process&#8217;s PID to the specified file.</p>
<dt><code>-p param=value</code></p>
<dd> Set the parameter specified by param to the specified value. See Run-Time Parameters for a list of parameters. This option can be used multiple times to specify multiple parameters.</p>
<dt><code>-r param[,param&#8230;]</code></p>
<dd> Make the listed parameters read only. This gives the system administrator a way to limit what the Varnish CLI can do. Consider making parameters such as <i>user</i>, <i>group</i>, <i>cc_command</i>, <i>vcc_allow_inline_c</i> read only as these can potentially be used to escalate privileges from the CLI. Protecting <i>listen_address</i> may also be a good idea.</p>
<dt><code>-s [name=]type[,options]</code></p>
<dd>
<dt><code>Use the specified storage backend. The storage backends can be one of the following:</code></p>
<dd>
<dt>&bull;</p>
<dd> malloc[,size]</p>
<dt>&bull;</p>
<dd> file[,path[,size[,granularity]]]</p>
<dt>&bull;</p>
<dd> persistent,path,size </p>
<p> See Storage Types in the Users Guide for more information on the various storage backends. This option can be used multiple times to specify multiple storage files. Names are referenced in logs, vcl, statistics, etc.</p>
<dt><code>-S</code><i>&nbsp;<wbr>file</i></p>
<dd> Path to a file containing a secret used for authorizing access to the management port.</p>
<dt><code>-T address[:port]</code></p>
<dd> Offer a management interface on the specified address and port. See Management Interface for a list of management commands.</p>
<dt><code>-t</code><i>&nbsp;<wbr>ttl</i></p>
<dd> Specifies a hard minimum time to live for cached documents. This is a shortcut for specifying the default_ttl run-time parameter.</p>
<dt><code>-u</code><i>&nbsp;<wbr>user</i></p>
<dd> Specifies the name of an unprivileged user to which the child process should switch before it starts accepting connections. This is a shortcut for specifying the user runtime parameter. </p>
<p> If specifying both a user and a group, the user should be specified first.</p>
<dt><code>-V</code></p>
<dd> Display the version number and exit.</dl>
<h3>Hash Algorithms</h3>
<p> The following hash algorithms are available:</p>
<dl>
<dt><code>critbit</code></p>
<dd>
<dt><code>A self-scaling tree structure. The default hash algorithm in</code></p>
<dd> Varnish Cache 2.1 and onwards. In comparison to a more traditional B tree the critbit tree is almost completely lockless. Do not change this unless you are certain what you&#8217;re doing.</p>
<dt><code>simple_list</code></p>
<dd> A simple doubly-linked list. Not recommended for production use.</p>
<dt><code>classic[,buckets]</code></p>
<dd> A standard hash table. The hash key is the CRC32 of the object&#8217;s URL modulo the size of the hash table. Each table entry points to a list of elements which share the same hash key. The buckets parameter specifies the number of entries in the hash table. The default is 16383.</dl>
<h3>Storage Types</h3>
<p> The following storage types are available:</p>
<h3>malloc</h3>
<p> syntax: malloc[,size] </p>
<p> malloc is a memory based backend.</p>
<h3>file</h3>
<p> syntax: file[,path[,size[,granularity]]] </p>
<p> The file backend stores data in a file on disk. The file will be accessed using mmap.</p>
<h3>persistent (experimental)</h3>
<p> syntax: persistent,path,size </p>
<p> Persistent storage. Varnish will store objects in a file in a manner that will secure the survival of <i>most</i> of the objects in the event of a planned or unplanned shutdown of Varnish. The persistent storage backend has multiple issues with it and will likely be removed from a future version of Varnish.</p>
<h3>Management Interface</h3>
<p> If the -T option was specified, varnishd will offer a command-line management interface on the specified address and port. The recommended way of connecting to the command-line management interface is through <a href="/docs/linux/man/1-varnishadm/">varnishadm</a>(1). </p>
<p> The commands available are documented in <a href="/docs/linux/man/7-varnish/">varnish</a>(7).</p>
<h3>Run-Time Parameters</h3>
<p> Runtime parameters are marked with shorthand flags to avoid repeating the same text over and over in the table below. The meaning of the flags are:</p>
<dl>
<dt><code>experimental</code></p>
<dd> We have no solid information about good/bad/optimal values for this parameter. Feedback with experience and observations are most welcome.</p>
<dt><code>delayed</code></p>
<dd> This parameter can be changed on the fly, but will not take effect immediately.</p>
<dt><code>restart</code></p>
<dd> The worker process must be stopped and restarted, before this parameter takes effect.</p>
<dt><code>reload</code></p>
<dd> The VCL programs must be reloaded for this parameter to take effect.</p>
<dt><code>experimental</code></p>
<dd> We&#8217;re not really sure about this parameter, tell us what you find.</p>
<dt><code>wizard</code></p>
<dd> Do not touch unless you <i>really</i> know what you&#8217;re doing.</p>
<dt><code>only_root</code></p>
<dd> Only works if varnishd is running as root. </p>
<p> Here is a list of all parameters, current as of last time we remembered to update the manual page. This text is produced from the same text you will find in the CLI if you use the param.show command, so should there be a new parameter which is not listed here, you can find the description using the CLI commands. </p>
<p> Be aware that on 32 bit systems, certain default values, such as workspace_client (=16k), thread_pool_workspace (=16k), http_resp_size (=8k), http_req_size (=12k), gzip_stack_buffer (=4k) and thread_pool_stack (=64k) are reduced relative to the values listed here, in order to conserve VM space.</dl>
<h3>acceptor_sleep_decay</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 0.9</p>
<dt>&bull;</p>
<dd> Minimum: 0</p>
<dt>&bull;</p>
<dd> Maximum: 1</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> If we run out of resources, such as file descriptors or worker threads, the acceptor will sleep between accepts. This parameter (multiplicatively) reduce the sleep duration for each successful accept. (ie: 0.9 = reduce by 10%)</dl>
<h3>acceptor_sleep_incr</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 0.001</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Maximum: 1.000</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> If we run out of resources, such as file descriptors or worker threads, the acceptor will sleep between accepts. This parameter control how much longer we sleep, each time we fail to accept a new connection.</dl>
<h3>acceptor_sleep_max</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 0.050</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Maximum: 10.000</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> If we run out of resources, such as file descriptors or worker threads, the acceptor will sleep between accepts. This parameter limits how long it can sleep between attempts to accept new connections.</dl>
<h3>auto_restart</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: on </p>
<p> Restart child process automatically if it dies.</dl>
<h3>ban_dups</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: on </p>
<p> Eliminate older identical bans when new bans are created. This test is CPU intensive and scales with the number and complexity of active (non-Gone) bans. If identical bans are frequent, the amount of CPU needed to actually test the bans will be similarly reduced.</dl>
<h3>ban_lurker_age</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 60.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> The ban lurker does not process bans until they are this old. Right when a ban is added, the most frequently hit objects will get tested against it as part of object lookup. This parameter prevents the ban-lurker from kicking in, until the rush is over.</dl>
<h3>ban_lurker_batch</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 1000</p>
<dt>&bull;</p>
<dd> Minimum: 1 </p>
<p> How many objects the ban lurker examines before taking a ban_lurker_sleep. Use this to pace the ban lurker so it does not eat too much CPU.</dl>
<h3>ban_lurker_sleep</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 0.010</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> The ban lurker thread sleeps between work batches, in order to not monopolize CPU power. When nothing is done, it sleeps a fraction of a second before looking for new work to do. A value of zero disables the ban lurker.</dl>
<h3>between_bytes_timeout</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 60.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> Default timeout between bytes when receiving data from backend. We only wait for this many seconds between bytes before giving up. A value of 0 means it will never time out. VCL can override this default value for each backend request and backend request. This parameter does not apply to pipe.</dl>
<h3>busyobj_worker_cache</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: off </p>
<p> Cache free busyobj per worker thread. Disable this if you have very high hitrates and want to save the memory of one busyobj per worker thread.</dl>
<h3>cc_command</h3>
<dl>
<dt>&bull;</p>
<dd> Default: &quot;exec gcc -std=gnu99 -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong &#8211;param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -Wall -Werror -Wno-error=unused-result -pthread -fpic -shared -Wl,-x -o %o %s&quot;</p>
<dt>&bull;</p>
<dd> Flags: must_reload </p>
<p> Command used for compiling the C source code to a <a href="/docs/linux/man/3-dlopen/">dlopen</a>(3) loadable object. Any occurrence of %s in the string will be replaced with the source file name, and %o will be replaced with the output file name.</dl>
<h3>cli_buffer</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 8k</p>
<dt>&bull;</p>
<dd> Minimum: 4k </p>
<p> Size of buffer for CLI command input. You may need to increase this if you have big VCL files and use the vcl.inline CLI command. NB: Must be specified with -p to have effect.</dl>
<h3>cli_limit</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 48k</p>
<dt>&bull;</p>
<dd> Minimum: 128b</p>
<dt>&bull;</p>
<dd> Maximum: 99999999b </p>
<p> Maximum size of CLI response. If the response exceeds this limit, the response code will be 201 instead of 200 and the last line will indicate the truncation.</dl>
<h3>cli_timeout</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 60.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> Timeout for the childs replies to CLI requests from the mgt_param.</dl>
<h3>clock_skew</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 10</p>
<dt>&bull;</p>
<dd> Minimum: 0 </p>
<p> How much clockskew we are willing to accept between the backend and our own clock.</dl>
<h3>connect_timeout</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 3.500</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> Default connection timeout for backend connections. We only try to connect to the backend for this many seconds before giving up. VCL can override this default value for each backend and backend request.</dl>
<h3>critbit_cooloff</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 180.000</p>
<dt>&bull;</p>
<dd> Minimum: 60.000</p>
<dt>&bull;</p>
<dd> Maximum: 254.000</p>
<dt>&bull;</p>
<dd> Flags: wizard </p>
<p> How long the critbit hasher keeps deleted objheads on the cooloff list.</dl>
<h3>debug</h3>
<dl>
<dt>&bull;</p>
<dd> Default: none </p>
<p> Enable/Disable various kinds of debugging.</p>
<dt><i>none</i></p>
<dd> Disable all debugging </p>
<p> Use +/- prefix to set/reset individual bits:</p>
<dt><i>req_state</i></p>
<dd> VSL Request state engine</p>
<dt><i>workspace</i></p>
<dd> VSL Workspace operations</p>
<dt><i>waiter</i></p>
<dd> VSL Waiter internals</p>
<dt><i>waitinglist</i></p>
<dd> VSL Waitinglist events</p>
<dt><i>syncvsl</i></p>
<dd> Make VSL synchronous</p>
<dt><i>hashedge</i></p>
<dd> Edge cases in Hash</p>
<dt><i>vclrel</i></p>
<dd> Rapid VCL release</p>
<dt><i>lurker</i></p>
<dd> VSL Ban lurker</p>
<dt><i>esi_chop</i></p>
<dd> Chop ESI fetch to bits</p>
<dt><i>flush_head</i></p>
<dd> Flush after http1 head</dl>
<h3>default_grace</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 10.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Flags: </p>
<p> Default grace period. We will deliver an object this long after it has expired, provided another thread is attempting to get a new copy.</dl>
<h3>default_keep</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 0.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Flags: </p>
<p> Default keep period. We will keep a useless object around this long, making it available for conditional backend fetches. That means that the object will be removed from the cache at the end of ttl+grace+keep.</dl>
<h3>default_ttl</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 120.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Flags: </p>
<p> The TTL assigned to objects if neither the backend nor the VCL code assigns one.</dl>
<h3>feature</h3>
<dl>
<dt>&bull;</p>
<dd> Default: none </p>
<p> Enable/Disable various minor features.</p>
<dt><i>none</i></p>
<dd> Disable all features. </p>
<p> Use +/- prefix to enable/disable individual feature:</p>
<dt><i>short_panic</i></p>
<dd> Short panic message.</p>
<dt><i>wait_silo</i></p>
<dd> Wait for persistent silo.</p>
<dt><i>no_coredump</i></p>
<dd> No coredumps.</p>
<dt><i>esi_ignore_https</i></p>
<dd> Treat HTTPS as HTTP in ESI:includes</p>
<dt><i>esi_disable_xml_check</i></p>
<dd> Don&#8217;t check of body looks like XML</p>
<dt><i>esi_ignore_other_elements</i></p>
<dd> Ignore non-esi XML-elements</p>
<dt><i>esi_remove_bom</i></p>
<dd> Remove UTF-8 BOM</dl>
<h3>fetch_chunksize</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 16k</p>
<dt>&bull;</p>
<dd> Minimum: 4k</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> The default chunksize used by fetcher. This should be bigger than the majority of objects with short TTLs. Internal limits in the storage_file module makes increases above 128kb a dubious idea.</dl>
<h3>fetch_maxchunksize</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 0.25G</p>
<dt>&bull;</p>
<dd> Minimum: 64k</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> The maximum chunksize we attempt to allocate from storage. Making this too large may cause delays and storage fragmentation.</dl>
<h3>first_byte_timeout</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 60.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> Default timeout for receiving first byte from backend. We only wait for this many seconds for the first byte before giving up. A value of 0 means it will never time out. VCL can override this default value for each backend and backend request. This parameter does not apply to pipe.</dl>
<h3>group</h3>
<dl>
<dt>&bull;</p>
<dd> Default: GID 425</p>
<dt>&bull;</p>
<dd> Flags: must_restart, only_root </p>
<p> The unprivileged group to run as.</dl>
<h3>group_cc</h3>
<dl>
<dt>&bull;</p>
<dd> Default: &lt;not set&gt;</p>
<dt>&bull;</p>
<dd> Flags: only_root </p>
<p> On some systems the C-compiler is restricted so not everybody can run it. This parameter makes it possible to add an extra group to the sandbox process which runs the cc_command, in order to gain access to such a restricted C-compiler.</dl>
<h3>gzip_buffer</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 32k</p>
<dt>&bull;</p>
<dd> Minimum: 2k</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> Size of malloc buffer used for gzip processing. These buffers are used for in-transit data, for instance gunzip&#8217;ed data being sent to a client.Making this space to small results in more overhead, writes to sockets etc, making it too big is probably just a waste of memory.</dl>
<h3>gzip_level</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 6</p>
<dt>&bull;</p>
<dd> Minimum: 0</p>
<dt>&bull;</p>
<dd> Maximum: 9 </p>
<p> Gzip compression level: 0=debug, 1=fast, 9=best</dl>
<h3>gzip_memlevel</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 8</p>
<dt>&bull;</p>
<dd> Minimum: 1</p>
<dt>&bull;</p>
<dd> Maximum: 9 </p>
<p> Gzip memory level 1=slow/least, 9=fast/most compression. Memory impact is 1=1k, 2=2k, &#8230; 9=256k.</dl>
<h3>http_gzip_support</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: on</p>
<dt><code>Enable gzip support. When enabled Varnish request compressed objects from the backend and store them compressed. If a client does not support gzip encoding Varnish will uncompress compressed objects on demand. Varnish will also rewrite the Accept-Encoding header of clients indicating support for gzip to:</code></p>
<dd> Accept-Encoding: gzip </p>
<p> Clients that do not support gzip will have their Accept-Encoding header removed. For more information on how gzip is implemented please see the chapter on gzip in the Varnish reference.</dl>
<h3>http_max_hdr</h3>
<dl>
<dt>&bull;</p>
<dd> Units: header lines</p>
<dt>&bull;</p>
<dd> Default: 64</p>
<dt>&bull;</p>
<dd> Minimum: 32</p>
<dt>&bull;</p>
<dd> Maximum: 65535 </p>
<p> Maximum number of HTTP header lines we allow in {req|resp|bereq|beresp}.http (obj.http is autosized to the exact number of headers). Cheap, ~20 bytes, in terms of workspace memory. Note that the first line occupies five header lines.</dl>
<h3>http_range_support</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: on </p>
<p> Enable support for HTTP Range headers.</dl>
<h3>http_req_hdr_len</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 8k</p>
<dt>&bull;</p>
<dd> Minimum: 40b </p>
<p> Maximum length of any HTTP client request header we will allow. The limit is inclusive its continuation lines.</dl>
<h3>http_req_size</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 32k</p>
<dt>&bull;</p>
<dd> Minimum: 0.25k </p>
<p> Maximum number of bytes of HTTP client request we will deal with. This is a limit on all bytes up to the double blank line which ends the HTTP request. The memory for the request is allocated from the client workspace (param: workspace_client) and this parameter limits how much of that the request is allowed to take up.</dl>
<h3>http_resp_hdr_len</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 8k</p>
<dt>&bull;</p>
<dd> Minimum: 40b </p>
<p> Maximum length of any HTTP backend response header we will allow. The limit is inclusive its continuation lines.</dl>
<h3>http_resp_size</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 32k</p>
<dt>&bull;</p>
<dd> Minimum: 0.25k </p>
<p> Maximum number of bytes of HTTP backend response we will deal with. This is a limit on all bytes up to the double blank line which ends the HTTP request. The memory for the request is allocated from the worker workspace (param: thread_pool_workspace) and this parameter limits how much of that the request is allowed to take up.</dl>
<h3>idle_send_timeout</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 60.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Flags: delayed </p>
<p> Time to wait with no data sent. If no data has been transmitted in this many seconds the session is closed. See <a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2) under SO_SNDTIMEO for more information.</dl>
<h3>listen_address</h3>
<dl>
<dt>&bull;</p>
<dd> Default: :80</p>
<dt>&bull;</p>
<dd> Flags: must_restart </p>
<p> Whitespace separated list of network endpoints where Varnish will accept requests. Possible formats: host, host:port, :port</dl>
<h3>listen_depth</h3>
<dl>
<dt>&bull;</p>
<dd> Units: connections</p>
<dt>&bull;</p>
<dd> Default: 1024</p>
<dt>&bull;</p>
<dd> Minimum: 0</p>
<dt>&bull;</p>
<dd> Flags: must_restart </p>
<p> Listen queue depth.</dl>
<h3>lru_interval</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 2.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> Grace period before object moves on LRU list. Objects are only moved to the front of the LRU list if they have not been moved there already inside this timeout period. This reduces the amount of lock operations necessary for LRU list access.</dl>
<h3>max_esi_depth</h3>
<dl>
<dt>&bull;</p>
<dd> Units: levels</p>
<dt>&bull;</p>
<dd> Default: 5</p>
<dt>&bull;</p>
<dd> Minimum: 0 </p>
<p> Maximum depth of esi:include processing.</dl>
<h3>max_restarts</h3>
<dl>
<dt>&bull;</p>
<dd> Units: restarts</p>
<dt>&bull;</p>
<dd> Default: 4</p>
<dt>&bull;</p>
<dd> Minimum: 0 </p>
<p> Upper limit on how many times a request can restart. Be aware that restarts are likely to cause a hit against the backend, so don&#8217;t increase thoughtlessly.</dl>
<h3>max_retries</h3>
<dl>
<dt>&bull;</p>
<dd> Units: retries</p>
<dt>&bull;</p>
<dd> Default: 4</p>
<dt>&bull;</p>
<dd> Minimum: 0 </p>
<p> Upper limit on how many times a backend fetch can retry.</dl>
<h3>nuke_limit</h3>
<dl>
<dt>&bull;</p>
<dd> Units: allocations</p>
<dt>&bull;</p>
<dd> Default: 50</p>
<dt>&bull;</p>
<dd> Minimum: 0</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> Maximum number of objects we attempt to nuke in orderto make space for a object body.</dl>
<h3>pcre_match_limit</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 10000</p>
<dt>&bull;</p>
<dd> Minimum: 1 </p>
<p> The limit for the number of internal matching function calls in a pcre_exec() execution.</dl>
<h3>pcre_match_limit_recursion</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 10000</p>
<dt>&bull;</p>
<dd> Minimum: 1 </p>
<p> The limit for the number of internal matching function recursions in a pcre_exec() execution.</dl>
<h3>ping_interval</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 3</p>
<dt>&bull;</p>
<dd> Minimum: 0</p>
<dt>&bull;</p>
<dd> Flags: must_restart </p>
<p> Interval between pings from parent to child. Zero will disable pinging entirely, which makes it possible to attach a debugger to the child.</dl>
<h3>pipe_timeout</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 60.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> Idle timeout for PIPE sessions. If nothing have been received in either direction for this many seconds, the session is closed.</dl>
<h3>pool_req</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 10,100,10 </p>
<p> Parameters for per worker pool request memory pool. The three numbers are:</p>
<dt><i>min_pool</i></p>
<dd> minimum size of free pool.</p>
<dt><i>max_pool</i></p>
<dd> maximum size of free pool.</p>
<dt><i>max_age</i></p>
<dd> max age of free element.</dl>
<h3>pool_sess</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 10,100,10 </p>
<p> Parameters for per worker pool session memory pool. The three numbers are:</p>
<dt><i>min_pool</i></p>
<dd> minimum size of free pool.</p>
<dt><i>max_pool</i></p>
<dd> maximum size of free pool.</p>
<dt><i>max_age</i></p>
<dd> max age of free element.</dl>
<h3>pool_vbc</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 10,100,10 </p>
<p> Parameters for backend connection memory pool. The three numbers are:</p>
<dt><i>min_pool</i></p>
<dd> minimum size of free pool.</p>
<dt><i>max_pool</i></p>
<dd> maximum size of free pool.</p>
<dt><i>max_age</i></p>
<dd> max age of free element.</dl>
<h3>pool_vbo</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 10,100,10 </p>
<p> Parameters for backend object fetch memory pool. The three numbers are:</p>
<dt><i>min_pool</i></p>
<dd> minimum size of free pool.</p>
<dt><i>max_pool</i></p>
<dd> maximum size of free pool.</p>
<dt><i>max_age</i></p>
<dd> max age of free element.</dl>
<h3>prefer_ipv6</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: off </p>
<p> Prefer IPv6 address when connecting to backends which have both IPv4 and IPv6 addresses.</dl>
<h3>rush_exponent</h3>
<dl>
<dt>&bull;</p>
<dd> Units: requests per request</p>
<dt>&bull;</p>
<dd> Default: 3</p>
<dt>&bull;</p>
<dd> Minimum: 2</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> How many parked request we start for each completed request on the object. NB: Even with the implict delay of delivery, this parameter controls an exponential increase in number of worker threads.</dl>
<h3>send_timeout</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 600.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Flags: delayed </p>
<p> Send timeout for client connections. If the HTTP response hasn&#8217;t been transmitted in this many seconds the session is closed. See <a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2) under SO_SNDTIMEO for more information.</dl>
<h3>session_max</h3>
<dl>
<dt>&bull;</p>
<dd> Units: sessions</p>
<dt>&bull;</p>
<dd> Default: 100000</p>
<dt>&bull;</p>
<dd> Minimum: 1000 </p>
<p> Maximum number of sessions we will allocate from one pool before just dropping connections. This is mostly an anti-DoS measure, and setting it plenty high should not hurt, as long as you have the memory for it.</dl>
<h3>shm_reclen</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 255b</p>
<dt>&bull;</p>
<dd> Minimum: 16b</p>
<dt>&bull;</p>
<dd> Maximum: 4084 </p>
<p> Old name for vsl_reclen, use that instead.</dl>
<h3>shortlived</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 10.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> Objects created with (ttl+grace+keep) shorter than this are always put in transient storage.</dl>
<h3>sigsegv_handler</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: off</p>
<dt>&bull;</p>
<dd> Flags: must_restart </p>
<p> Install a signal handler which tries to dump debug information on segmentation faults.</dl>
<h3>syslog_cli_traffic</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: on </p>
<p> Log all CLI traffic to syslog(LOG_INFO).</dl>
<h3>tcp_keepalive_intvl</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 75.000</p>
<dt>&bull;</p>
<dd> Minimum: 1.000</p>
<dt>&bull;</p>
<dd> Maximum: 100.000</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> The number of seconds between TCP keep-alive probes.</dl>
<h3>tcp_keepalive_probes</h3>
<dl>
<dt>&bull;</p>
<dd> Units: probes</p>
<dt>&bull;</p>
<dd> Default: 9</p>
<dt>&bull;</p>
<dd> Minimum: 1</p>
<dt>&bull;</p>
<dd> Maximum: 100</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> The maximum number of TCP keep-alive probes to send before giving up and killing the connection if no response is obtained from the other end.</dl>
<h3>tcp_keepalive_time</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 7200.000</p>
<dt>&bull;</p>
<dd> Minimum: 1.000</p>
<dt>&bull;</p>
<dd> Maximum: 7200.000</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> The number of seconds a connection needs to be idle before TCP begins sending out keep-alive probes.</dl>
<h3>thread_pool_add_delay</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 0.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> Wait at least this long after creating a thread. </p>
<p> Some (buggy) systems may need a short (sub-second) delay between creating threads. Set this to a few milliseconds if you see the &#8216;threads_failed&#8217; counter grow too much. </p>
<p> Setting this too high results in insuffient worker threads.</dl>
<h3>thread_pool_destroy_delay</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 1.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.010</p>
<dt>&bull;</p>
<dd> Flags: delayed, experimental </p>
<p> Wait this long after destroying a thread. </p>
<p> This controls the decay of thread pools when idle(-ish). </p>
<p> Minimum is 0.01 seconds.</dl>
<h3>thread_pool_fail_delay</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 0.200</p>
<dt>&bull;</p>
<dd> Minimum: 0.010</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> Wait at least this long after a failed thread creation before trying to create another thread. </p>
<p> Failure to create a worker thread is often a sign that the end is near, because the process is running out of some resource. This delay tries to not rush the end on needlessly. </p>
<p> If thread creation failures are a problem, check that thread_pool_max is not too high. </p>
<p> It may also help to increase thread_pool_timeout and thread_pool_min, to reduce the rate at which treads are destroyed and later recreated.</dl>
<h3>thread_pool_max</h3>
<dl>
<dt>&bull;</p>
<dd> Units: threads</p>
<dt>&bull;</p>
<dd> Default: 5000</p>
<dt>&bull;</p>
<dd> Minimum: 100</p>
<dt>&bull;</p>
<dd> Flags: delayed </p>
<p> The maximum number of worker threads in each pool. </p>
<p> Do not set this higher than you have to, since excess worker threads soak up RAM and CPU and generally just get in the way of getting work done. </p>
<p> Minimum is 10 threads.</dl>
<h3>thread_pool_min</h3>
<dl>
<dt>&bull;</p>
<dd> Units: threads</p>
<dt>&bull;</p>
<dd> Default: 100</p>
<dt>&bull;</p>
<dd> Maximum: 5000</p>
<dt>&bull;</p>
<dd> Flags: delayed </p>
<p> The minimum number of worker threads in each pool. </p>
<p> Increasing this may help ramp up faster from low load situations or when threads have expired. </p>
<p> Minimum is 10 threads.</dl>
<h3>thread_pool_stack</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 48k</p>
<dt>&bull;</p>
<dd> Minimum: 16k</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> Worker thread stack size. This will likely be rounded up to a multiple of 4k (or whatever the page_size might be) by the kernel.</dl>
<h3>thread_pool_timeout</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 300.000</p>
<dt>&bull;</p>
<dd> Minimum: 10.000</p>
<dt>&bull;</p>
<dd> Flags: delayed, experimental </p>
<p> Thread idle threshold. </p>
<p> Threads in excess of thread_pool_min, which have been idle for at least this long, will be destroyed. </p>
<p> Minimum is 10 seconds.</dl>
<h3>thread_pools</h3>
<dl>
<dt>&bull;</p>
<dd> Units: pools</p>
<dt>&bull;</p>
<dd> Default: 2</p>
<dt>&bull;</p>
<dd> Minimum: 1</p>
<dt>&bull;</p>
<dd> Flags: delayed, experimental </p>
<p> Number of worker thread pools. </p>
<p> Increasing number of worker pools decreases lock contention. </p>
<p> Too many pools waste CPU and RAM resources, and more than one pool for each CPU is probably detrimal to performance. </p>
<p> Can be increased on the fly, but decreases require a restart to take effect.</dl>
<h3>thread_queue_limit</h3>
<dl>
<dt>&bull;</p>
<dd> Default: 20</p>
<dt>&bull;</p>
<dd> Minimum: 0</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> Permitted queue length per thread-pool. </p>
<p> This sets the number of requests we will queue, waiting for an available thread. Above this limit sessions will be dropped instead of queued.</dl>
<h3>thread_stats_rate</h3>
<dl>
<dt>&bull;</p>
<dd> Units: requests</p>
<dt>&bull;</p>
<dd> Default: 10</p>
<dt>&bull;</p>
<dd> Minimum: 0</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> Worker threads accumulate statistics, and dump these into the global stats counters if the lock is free when they finish a job (request/fetch etc.) This parameters defines the maximum number of jobs a worker thread may handle, before it is forced to dump its accumulated stats into the global counters.</dl>
<h3>timeout_idle</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 5.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> Idle timeout for client connections. A connection is considered idle, until we receive a non-white-space character on it.</dl>
<h3>timeout_linger</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 0.050</p>
<dt>&bull;</p>
<dd> Minimum: 0.000</p>
<dt>&bull;</p>
<dd> Flags: experimental </p>
<p> How long the worker thread lingers on an idle session before handing it over to the waiter. When sessions are reused, as much as half of all reuses happen within the first 100 msec of the previous request completing. Setting this too high results in worker threads not doing anything for their keep, setting it too low just means that more sessions take a detour around the waiter.</dl>
<h3>timeout_req</h3>
<dl>
<dt>&bull;</p>
<dd> Units: seconds</p>
<dt>&bull;</p>
<dd> Default: 2.000</p>
<dt>&bull;</p>
<dd> Minimum: 0.000 </p>
<p> Max time to receive clients request headers, measured from first non-white-space character to double CRNL.</dl>
<h3>user</h3>
<dl>
<dt>&bull;</p>
<dd> Default: nobody (99)</p>
<dt>&bull;</p>
<dd> Flags: must_restart, only_root </p>
<p> The unprivileged user to run as.</dl>
<h3>vcc_allow_inline_c</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: off </p>
<p> Allow inline C code in VCL.</dl>
<h3>vcc_err_unref</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: on </p>
<p> Unreferenced VCL objects result in error.</dl>
<h3>vcc_unsafe_path</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bool</p>
<dt>&bull;</p>
<dd> Default: on </p>
<p> Allow &#8216;/&#8217; in vmod &amp; include paths. Allow &#8216;import &#8230; from &#8230;&#8217;.</dl>
<h3>vcl_dir</h3>
<dl>
<dt>&bull;</p>
<dd> Default: /etc/varnish </p>
<p> Directory from which relative VCL filenames (vcl.load and include) are opened.</dl>
<h3>vmod_dir</h3>
<dl>
<dt>&bull;</p>
<dd> Default: /usr/lib64/varnish/vmods </p>
<p> Directory where VCL modules are to be found.</dl>
<h3>vsl_buffer</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 4k</p>
<dt>&bull;</p>
<dd> Minimum: 267 </p>
<p> Bytes of (req-/backend-)workspace dedicated to buffering VSL records. Setting this too high costs memory, setting it too low will cause more VSL flushes and likely increase lock-contention on the VSL mutex. </p>
<p> The minimum tracks the vsl_reclen parameter + 12 bytes.</dl>
<h3>vsl_mask</h3>
<dl>
<dt>&bull;</p>
<dd> Default: -VCL_trace,-WorkThread,-Hash </p>
<p> Mask individual VSL messages from being logged.</p>
<dt><i>default</i></p>
<dd> Set default value </p>
<p> Use +/- prefixe in front of VSL tag name, to mask/unmask individual VSL messages.</dl>
<h3>vsl_reclen</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 255b</p>
<dt>&bull;</p>
<dd> Minimum: 16b</p>
<dt>&bull;</p>
<dd> Maximum: 4084b </p>
<p> Maximum number of bytes in SHM log record. </p>
<p> The maximum tracks the vsl_buffer parameter &#8211; 12 bytes.</dl>
<h3>vsl_space</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 80M</p>
<dt>&bull;</p>
<dd> Minimum: 1M</p>
<dt>&bull;</p>
<dd> Flags: must_restart </p>
<p> The amount of space to allocate for the VSL fifo buffer in the VSM memory segment. If you make this too small, varnish{ncsa|log} etc will not be able to keep up. Making it too large just costs memory resources.</dl>
<h3>vsm_space</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 1M</p>
<dt>&bull;</p>
<dd> Minimum: 1M</p>
<dt>&bull;</p>
<dd> Flags: must_restart </p>
<p> The amount of space to allocate for stats counters in the VSM memory segment. If you make this too small, some counters will be invisible. Making it too large just costs memory resources.</dl>
<h3>waiter</h3>
<dl>
<dt>&bull;</p>
<dd> Default: epoll (possible values: epoll, poll)</p>
<dt>&bull;</p>
<dd> Flags: must_restart, wizard </p>
<p> Select the waiter kernel interface.</dl>
<h3>workspace_backend</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 64k</p>
<dt>&bull;</p>
<dd> Minimum: 1k</p>
<dt>&bull;</p>
<dd> Flags: delayed </p>
<p> Bytes of HTTP protocol workspace for backend HTTP req/resp. If larger than 4k, use a multiple of 4k for VM efficiency.</dl>
<h3>workspace_client</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 64k</p>
<dt>&bull;</p>
<dd> Minimum: 9k</p>
<dt>&bull;</p>
<dd> Flags: delayed </p>
<p> Bytes of HTTP protocol workspace for clients HTTP req/resp. If larger than 4k, use a multiple of 4k for VM efficiency.</dl>
<h3>workspace_session</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 384b</p>
<dt>&bull;</p>
<dd> Minimum: 0.25k</p>
<dt>&bull;</p>
<dd> Flags: delayed </p>
<p> Bytes of workspace for session and TCP connection addresses. If larger than 4k, use a multiple of 4k for VM efficiency.</dl>
<h3>workspace_thread</h3>
<dl>
<dt>&bull;</p>
<dd> Units: bytes</p>
<dt>&bull;</p>
<dd> Default: 2k</p>
<dt>&bull;</p>
<dd> Minimum: 0.25k</p>
<dt>&bull;</p>
<dd> Maximum: 8k</p>
<dt>&bull;</p>
<dd> Flags: delayed </p>
<p> Bytes of auxiliary workspace per thread. This workspace is used for certain temporary data structures during the operation of a worker thread. One use is for the io-vectors for writing requests and responses to sockets, having too little space will result in more <a href="/docs/linux/man/2-writev/">writev</a>(2) system calls, having too much just wastes the space.</dl>
<h2>EXIT CODES</h2>
<p> Varnish and bundled tools will, in most cases, exit with one of the following codes</p>
<dl>
<dt>&bull;</p>
<dd> <i>0</i> OK</p>
<dt>&bull;</p>
<dd> <i>1</i> Some error which could be system-dependend and/or transient</p>
<dt>&bull;</p>
<dd> <i>2</i> Serious configuration / parameter error &#8211; retrying with the same configuration / parameters is most likely useless </p>
<p> The <i>varnishd</i> master process may also OR its exit code</p>
<dt>&bull;</p>
<dd> with <i>0x20</i> when the <i>varnishd</i> child process died,</p>
<dt>&bull;</p>
<dd> with <i>0x40</i> when the <i>varnishd</i> child process was terminated by a signal and</p>
<dt>&bull;</p>
<dd> with <i>0x80</i> when a core was dumped.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/7-varnish-cli/">varnish-cli</a>(7)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishlog/">varnishlog</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishhist/">varnishhist</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishncsa/">varnishncsa</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishstat/">varnishstat</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishtop/">varnishtop</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/7-vcl/">vcl</a>(7)</dl>
<h2>HISTORY</h2>
<p> The varnishd daemon was developed by Poul-Henning Kamp in cooperation with Verdens Gang AS and Varnish Software. </p>
<p> This manual page was written by Dag-Erling Smørgrav with updates by Stig Sandbeck Mathisen &lt;<i>ssm [at] debian.org</i>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
<dl>
<dt>&bull;</p>
<dd> Copyright (c) 2007-2014 Varnish Software AS </p>
</dl>
<h2>Index</h2>
