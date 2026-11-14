---
title: "dapltest(1)"
name: "dapltest"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dapltest/"
description: "dapltest – test for the Direct Access Programming Library (DAPL)"
---

<h2 class="name">NAME</h2>
<p> <code> dapltest </code>&#8211; test for the Direct Access Programming Library (DAPL) </p>
<h2>DESCRIPTION</h2>
<p> Dapltest is a set of tests developed to exercise, characterize, and verify the DAPL interfaces during development and porting. At least two instantiations of the test must be run. One acts as the server, fielding requests and spawning server-side test threads as needed. Other client invocations connect to the server and issue test requests. The server side of the test, once invoked, listens continuously for client connection requests, until quit or killed. Upon receipt of a connection request, the connection is established, the server and client sides swap version numbers to verify that they are able to communicate, and the client sends the test request to the server. If the version numbers match, and the test request is well-formed, the server spawns the threads needed to run the test before awaiting further connections.</p>
<h2>USAGE</h2>
<p> dapltest [ -f script_file_name ] [ -T S|Q|T|P|L ] [ -D device_name ] [-n port_number] [ -d ] [ -R HT|LL|EC|PM|BE ] </p>
<p> With no arguments, dapltest runs as a server using default values, and loops accepting requests from clients. </p>
<p> The -f option allows all arguments to be placed in a file, to ease test automation. </p>
<p> The following arguments are common to all tests:</p>
<dl>
<dt><code>[ -T S|Q|T|P|L ]</code></p>
<dd> Test function to be performed:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>S</code></p>
<dd> &#8211; server loop</p>
<dt><code>Q</code></p>
<dd> &#8211; quit, client requests that server wait for any outstanding tests to complete, then clean up and exit</p>
<dt><code>T</code></p>
<dd> &#8211; transaction test, transfers data between client and server</p>
<dt><code>P</code></p>
<dd> &#8211; performance test, times DTO operations</p>
<dt><code>L</code></p>
<dd> &#8211; limit test, exhausts various resources, runs in client w/o server interaction Default: S</dl>
</dl>
<dt><code>[ -D device_name ]</code></p>
<dd> Specifies the interface adapter name as documented in the /etc/dat.conf static configuration file. This name corresponds to the provider library to open. Default: none</p>
<dt><code>[ -n server_port_number]</code></p>
<dd> Specifies the starting server port for all tests. Default: 45278</p>
<dt><code>[ -d ]</code></p>
<dd> Enables extra debug verbosity, primarily tracing of the various DAPL operations as they progress. Repeating this parameter increases debug spew. Errors encountered result in the test spewing some explanatory text and stopping; this flag provides more detail about what lead up to the error. Default: zero</p>
<dt><code>[ -R BE ]</code></p>
<dd> Indicate the quality of service (QoS) desired. Choices are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>HT</code></p>
<dd> &#8211; high throughput</p>
<dt><code>LL</code></p>
<dd> &#8211; low latency</p>
<dt><code>EC</code></p>
<dd> &#8211; economy (neither HT nor LL)</p>
<dt><code>PM</code></p>
<dd> &#8211; premium</p>
<dt><code>BE</code></p>
<dd> &#8211; best effort Default: BE</dl>
</dl>
</dl>
<p> <code>Usage &#8211; Quit test client</code> </p>
<pre><code>
    dapltest [Common_Args] [ -s server_name ]
    Quit testing (-T Q) connects to the server to ask it to clean up and
    exit (after it waits for any outstanding test runs to complete).
    In addition to being more polite than simply killing the server,
    this test exercises the DAPL object teardown code paths.
    There is only one argument other than those supported by all tests:
    -s server_name      Specifies the name of the server interface.
                        No default.
</code></pre>
<p> <code>Usage &#8211; Transaction test client</code> </p>
<p>    dapltest [Common_Args] [ -s server_name ]<br />
             [ -t threads ] [ -w endpoints ] [ -i iterations ] [ -Q ]<br />
             [ -V ] [ -P ] OPclient OPserver [ op3,<br />
    Transaction testing (-T T) transfers a variable amount of data between<br />
    client and server.  The data transfer can be described as a sequence of<br />
    individual operations; that entire sequence is transferred &#8216;iterations&#8217;<br />
    times by each thread over all of its endpoint(s).<br />
    The following parameters determine the behavior of the transaction test:<br />
    -s server_name      Specifies the name or IP address of the server interface.<br />
                        No default.<br />
    [ -t threads ]      Specify the number of threads to be used.<br />
                        Default: 1<br />
    [ -w endpoints ]    Specify the number of connected endpoints per thread.<br />
                        Default: 1<br />
    [ -i iterations ]   Specify the number of times the entire sequence<br />
                        of data transfers will be made over each endpoint.<br />
                        Default: 1000<br />
    [ -Q ]              Funnel completion events into a CNO.<br />
                        Default: use EVDs<br />
    [ -V ]              Validate the data being transferred.<br />
                        Default: ignore the data<br />
    [ -P ]              Turn on DTO completion polling<br />
                        Default: off<br />
    OP1 OP2 [ OP3, &#8230; ]<br />
                        A single transaction (OPx) consists of:<br />
                        server|client   Indicates who initiates the<br />
                                        data transfer.<br />
                        SR|RR|RW        Indicates the type of transfer:<br />
                                        SR  send/recv<br />
                                        RR  RDMA read<br />
                                        RW  RDMA write<br />
                        Defaults: none<br />
                        [ seg_size [ num_segs ] ]<br />
                                        Indicates the amount and format<br />
                                        of the data to be transferred.<br />
                                        Default:  4096  1<br />
                                                  (i.e., 1 4KB buffer)<br />
                        [ -f ]          For SR transfers only, indicates<br />
                                        that a client&#8217;s send transfer<br />
                                        completion should be reaped when<br />
                                        the next recv completion is reaped.<br />
                                        Sends and receives must be paired<br />
                                        (one client, one server, and in that<br />
                                        order) for this option to be used.<br />
    Restrictions:<br />
    Due to the flow control algorithm used by the transaction test, there<br />
    must be at least one SR OP for both the client and the server.<br />
    Requesting data validation (-V) causes the test to automatically append<br />
    three OPs to those specified. These additional operations provide<br />
    synchronization points during each iteration, at which all user-specified<br />
    transaction buffers are checked. These three appended operations satisfy<br />
    the &#8220;one SR in each direction&#8221; requirement.<br />
    The transaction OP list is printed out if -d is supplied.<br />
 <code>Usage &#8211; Performance test client</code> </p>
<pre><code>
    dapltest [Common_Args] -s server_name [ -m p|b ]
             [ -i iterations ] [ -p pipeline ] OP
    Performance testing (-T P) times the transfer of an operation.
    The operation is posted 'iterations' times.
    The following parameters determine the behavior of the transaction test:
    -s server_name      Specifies the name or IP address of the server interface.
                        No default.
    -m b|p              Used to choose either blocking (b) or polling (p)
                        Default: blocking (b)
    [ -i iterations ]   Specify the number of times the entire sequence
                        of data transfers will be made over each endpoint.
                        Default: 1000
    [ -p pipeline ]     Specify the pipline length, valid arguments are in 
                        the range [0,MAX_SEND_DTOS]. If a value greater than 
                        MAX_SEND_DTOS is requested the value will be
                        adjusted down to MAX_SEND_DTOS.
                        Default: MAX_SEND_DTOS
                        
    OP                  Specifies the operation as follow:                 
                        RR|RW           Indicates the type of transfer:
                                        RR  RDMA read
                                        RW  RDMA write
                                        Defaults: none
                        [ seg_size [ num_segs ] ]
                                        Indicates the amount and format
                                        of the data to be transferred.
                                        Default:  4096  1
                                                  (i.e., 1 4KB buffer)
Usage - Limit test client
    Limit testing (-T L) neither requires nor connects to any server
    instance.  The client runs one or more tests which attempt to
    exhaust various resources to determine DAPL limits and exercise
    DAPL error paths.  If no arguments are given, all tests are run.
    Limit testing creates the sequence of DAT objects needed to
    move data back and forth, attempting to find the limits supported
    for the DAPL object requested.  For example, if the LMR creation
    limit is being examined, the test will create a set of
    {IA, PZ, CNO, EVD, EP} before trying to run dat_lmr_create() to
    failure using that set of DAPL objects.  The 'width' parameter
    can be used to control how many of these parallel DAPL object
    sets are created before beating upon the requested constructor.
    Use of -m limits the number of dat_*_create() calls that will
    be attempted, which can be helpful if the DAPL in use supports
    essentailly unlimited numbers of some objects.
    The limit test arguments are:
    [ -m maximum ]      Specify the maximum number of dapl_*_create()
                        attempts.
                        Default: run to object creation failure
    [ -w width ]        Specify the number of DAPL object sets to
                        create while initializing.
                        Default: 1
    [ limit_ia ]        Attempt to exhaust dat_ia_open()
    [ limit_pz ]        Attempt to exhaust dat_pz_create()
    [ limit_cno ]       Attempt to exhaust dat_cno_create()
    [ limit_evd ]       Attempt to exhaust dat_evd_create()
    [ limit_ep ]        Attempt to exhaust dat_ep_create()
    [ limit_rsp ]       Attempt to exhaust dat_rsp_create()
    [ limit_psp ]       Attempt to exhaust dat_psp_create()
    [ limit_lmr ]       Attempt to exhaust dat_lmr_create(4KB)
    [ limit_rpost ]     Attempt to exhaust dat_ep_post_recv(4KB)
    [ limit_size_lmr ]  Probe maximum size dat_lmr_create()
                        Default: run all tests
</code></pre>
<h2>EXAMPLES</h2>
<p> dapltest -T S -d -D OpenIB-cma -n 53000 </p>
<pre>
                        Starts a server process with debug verbosity, on server port 53000.
</pre>
<p> dapltest -T T -d -s host1-ib0 -D OpenIB-cma -n 53000 -i 100 client SR 4096 2 server SR 4096 2 </p>
<pre>
                        Runs a transaction test, with both sides
                        sending one buffer with two 4KB segments,
                        one hundred times. To server host1-ib0 on port 53000
</pre>
<p> dapltest -T P -d -s host1-ib0 -D OpenIB-cma -i 100 RW 4096 2 </p>
<pre>
                        Runs a performance test, with the client 
                        sending one buffer with two 4KB segments,
                        one hundred times.
</pre>
<p> dapltest -T Q -s host1-ib0 -D OpenIB-cma </p>
<pre>
                        Asks the server to clean up and exit.
</pre>
<p> dapltest -T L -D OpenIB-cma -d -w 16 -m 1000 </p>
<pre>
                        Runs all of the limit tests, setting up
                        16 complete sets of DAPL objects, and
                        creating at most a thousand instances
                        when trying to exhaust resources.
</pre>
<p> dapltest -T T -V -d -t 2 -w 4 -i 55555 -s linux3 -D OpenIB-cma client RW 4096 1 server RW 2048 4 client SR 1024 4 server SR 4096 2 client SR 1024 3 -f server SR 2048 1 -f </p>
<pre>
                        Runs a more complicated transaction test,
                        with two thread using four EPs each,
                        sending a more complicated buffer pattern
                        for a larger number of iterations,
                        validating the data received.
</pre>
<dl>
<dt><code>BUGS</code></p>
<dd> (and To Do List)</dl>
<pre>
    Use of CNOs (-Q) is not yet supported.
    Further limit tests could be added.
</pre>
<h2>Index</h2>
