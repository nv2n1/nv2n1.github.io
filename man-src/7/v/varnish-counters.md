---
title: "varnish-counters(7)"
name: "varnish-counters"
section: "7"
letter: "v"
url: "/docs/linux/man/7-varnish-counters/"
description: "varnish-counters – Varnish counter field definitions"
---

<p>varnish-counters &#8211; Varnish counter field definitions</p>
<h2>Counter Levels</h2>
<dl>
<dt><code>INFO – Informational counters</code></p>
<dd>Counters giving runtime information</p>
<dt><code>DIAG – Diagnostic counters</code></p>
<dd>Counters giving diagnostic information</p>
<dt><code>DEBUG – Debug counters</code></p>
<dd>Counters giving Varnish internals debug information</dl>
<h2>Main Counters</h2>
<dl>
<dt><code>uptime – Child process uptime (INFO)</code></p>
<dd>How long the child process has been running.</p>
<dt><code>sess_conn – Sessions accepted (INFO)</code></p>
<dd>Count of sessions successfully accepted</p>
<dt><code>sess_drop – Sessions dropped (INFO)</code></p>
<dd>Count of sessions silently dropped due to lack of worker thread.</p>
<dt><code>sess_fail – Session accept failures (INFO)</code></p>
<dd>Count of failures to accept TCP connection. Either the client changed its mind, or the kernel ran out of some resource like file descriptors.</p>
<dt><code>sess_pipe_overflow – Session pipe overflow (INFO)</code></p>
<dd>Count of sessions dropped due to the session pipe overflowing.</p>
<dt><code>client_req_400 – Client requests received, subject to 400 errors (INFO)</code></p>
<dd>400 means we couldn&#8217;t make sense of the request, it was malformed in some drastic way.</p>
<dt><code>client_req_411 – Client requests received, subject to 411 errors (INFO)</code></p>
<dd>411 means the client did not send a Content-Lenght for the req.body.</p>
<dt><code>client_req_413 – Client requests received, subject to 413 errors (INFO)</code></p>
<dd>413 means that HTTP headers exceeded length or count limits.</p>
<dt><code>client_req_417 – Client requests received, subject to 417 errors (INFO)</code></p>
<dd>417 means that something went wrong with an Expect: header.</p>
<dt><code>client_req – Good client requests received (INFO)</code></p>
<dd>The count of parseable client requests seen.</p>
<dt><code>cache_hit – Cache hits (INFO)</code></p>
<dd>Count of cache hits. A cache hit indicates that an object has been delivered to a client without fetching it from a backend server.</p>
<dt><code>cache_hitpass – Cache hits for pass (INFO)</code></p>
<dd>Count of hits for pass A cache hit for pass indicates that Varnish is going to pass the request to the backend and this decision has been cached in it self. This counts how many times the cached decision is being used.</p>
<dt><code>cache_miss – Cache misses (INFO)</code></p>
<dd>Count of misses A cache miss indicates the object was fetched from the backend before delivering it to the backend.</p>
<dt><code>backend_conn – Backend conn. success (INFO)</code></p>
<dd>How many backend connections have successfully been established. </p>
<p> backend_unhealthy – Backend conn. not attempted (INFO) </p>
<p> backend_busy – Backend conn. too many (INFO) </p>
<p> backend_fail – Backend conn. failures (INFO)</p>
<dt><code>backend_reuse – Backend conn. reuses (INFO)</code></p>
<dd>Count of backend connection reuses This counter is increased whenever we reuse a recycled connection. </p>
<p> backend_toolate – Backend conn. was closed (INFO)</p>
<dt><code>backend_recycle – Backend conn. recycles (INFO)</code></p>
<dd>Count of backend connection recycles This counter is increased whenever we have a keep-alive connection that is put back into the pool of connections. It has not yet been used, but it might be, unless the backend closes it. </p>
<p> backend_retry – Backend conn. retry (INFO)</p>
<dt><code>fetch_head – Fetch no body (HEAD) (INFO)</code></p>
<dd>beresp with no body because the request is HEAD.</p>
<dt><code>fetch_length – Fetch with Length (INFO)</code></p>
<dd>beresp with Content-Length.</p>
<dt><code>fetch_chunked – Fetch chunked (INFO)</code></p>
<dd>beresp with Chunked.</p>
<dt><code>fetch_eof – Fetch EOF (INFO)</code></p>
<dd>beresp with EOF from lack of other info.</p>
<dt><code>fetch_bad – Fetch bad T-E (INFO)</code></p>
<dd>beresp failed due to unknown Transfer-Encoding.</p>
<dt><code>fetch_close – Fetch wanted close (INFO)</code></p>
<dd>beresp with EOF due to Connection: Close.</p>
<dt><code>fetch_oldhttp – Fetch pre HTTP/1.1 closed (INFO)</code></p>
<dd>beresp with EOF due to HTTP &lt; 1.1</p>
<dt><code>fetch_zero – Fetch zero len body (INFO)</code></p>
<dd>beresp with EOF due to keep-live but neither Chunked or Len.</p>
<dt><code>fetch_1xx – Fetch no body (1xx) (INFO)</code></p>
<dd>beresp with no body because of 1XX response.</p>
<dt><code>fetch_204 – Fetch no body (204) (INFO)</code></p>
<dd>beresp with no body because of 204 response.</p>
<dt><code>fetch_304 – Fetch no body (304) (INFO)</code></p>
<dd>beresp with no body because of 304 response.</p>
<dt><code>fetch_failed – Fetch failed (all causes) (INFO)</code></p>
<dd>beresp fetch failed.</p>
<dt><code>fetch_no_thread – Fetch failed (no thread) (INFO)</code></p>
<dd>beresp fetch failed, no thread available.</p>
<dt><code>pools – Number of thread pools (INFO)</code></p>
<dd>Number of thread pools. See also parameter thread_pools. NB: Presently pools cannot be removed once created.</p>
<dt><code>threads – Total number of threads (INFO)</code></p>
<dd>Number of threads in all pools. See also parameters thread_pools, thread_pool_min and thread_pool_max.</p>
<dt><code>threads_limited – Threads hit max (INFO)</code></p>
<dd>Number of times more threads were needed, but limit was reached in a thread pool. See also parameter thread_pool_max.</p>
<dt><code>threads_created – Threads created (INFO)</code></p>
<dd>Total number of threads created in all pools.</p>
<dt><code>threads_destroyed – Threads destroyed (INFO)</code></p>
<dd>Total number of threads destroyed in all pools.</p>
<dt><code>threads_failed – Thread creation failed (INFO)</code></p>
<dd>Number of times creating a thread failed. See VSL::Debug for diagnostics. See also parameter thread_fail_delay.</p>
<dt><code>thread_queue_len – Length of session queue (INFO)</code></p>
<dd>Length of session queue waiting for threads. NB: Only updates once per second. See also parameter queue_max.</p>
<dt><code>busy_sleep – Number of requests sent to sleep on busy objhdr (INFO)</code></p>
<dd>Number of requests sent to sleep without a worker thread because they found a busy object.</p>
<dt><code>busy_wakeup – Number of requests woken after sleep on busy objhdr (INFO)</code></p>
<dd>Number of requests taken of the busy object sleep list and and rescheduled.</p>
<dt><code>sess_queued – Sessions queued for thread (INFO)</code></p>
<dd>Number of times session was queued waiting for a thread. See also parameter queue_max.</p>
<dt><code>sess_dropped – Sessions dropped for thread (INFO)</code></p>
<dd>Number of times session was dropped because the queue were too long already. See also parameter queue_max.</p>
<dt><code>n_object – object structs made (INFO)</code></p>
<dd>Number of object structs made</p>
<dt><code>n_vampireobject – unresurrected objects (DIAG)</code></p>
<dd>Number of unresurrected objects</p>
<dt><code>n_objectcore – objectcore structs made (INFO)</code></p>
<dd>Number of objectcore structs made</p>
<dt><code>n_objecthead – objecthead structs made (INFO)</code></p>
<dd>Number of objecthead structs made</p>
<dt><code>n_waitinglist – waitinglist structs made (DEBUG)</code></p>
<dd>Number of waitinglist structs made</p>
<dt><code>n_backend – Number of backends (INFO)</code></p>
<dd>Number of backends known to us.</p>
<dt><code>n_expired – Number of expired objects (INFO)</code></p>
<dd>Number of objects that expired from cache because of old age.</p>
<dt><code>n_lru_nuked – Number of LRU nuked objects (INFO)</code></p>
<dd>How many objects have been forcefully evicted from storage to make room for a new object.</p>
<dt><code>n_lru_moved – Number of LRU moved objects (DIAG)</code></p>
<dd>Number of move operations done on the LRU list. </p>
<p> losthdr – HTTP header overflows (INFO) </p>
<p> s_sess – Total sessions seen (INFO) </p>
<p> s_req – Total requests seen (INFO) </p>
<p> s_pipe – Total pipe sessions seen (INFO) </p>
<p> s_pass – Total pass-ed requests seen (INFO) </p>
<p> s_fetch – Total backend fetches initiated (INFO) </p>
<p> s_synth – Total synthethic responses made (INFO)</p>
<dt><code>s_req_hdrbytes – Request header bytes (INFO)</code></p>
<dd>Total request header bytes received</p>
<dt><code>s_req_bodybytes – Request body bytes (INFO)</code></p>
<dd>Total request body bytes received</p>
<dt><code>s_resp_hdrbytes – Response header bytes (INFO)</code></p>
<dd>Total response header bytes transmitted</p>
<dt><code>s_resp_bodybytes – Response body bytes (INFO)</code></p>
<dd>Total response body bytes transmitted</p>
<dt><code>s_pipe_hdrbytes – Pipe request header bytes (INFO)</code></p>
<dd>Total request bytes received for piped sessions</p>
<dt><code>s_pipe_in – Piped bytes from client (INFO)</code></p>
<dd>Total number of bytes forwarded from clients in pipe sessions</p>
<dt><code>s_pipe_out – Piped bytes to client (INFO)</code></p>
<dd>Total number of bytes forwarded to clients in pipe sessions </p>
<p> sess_closed – Session Closed (INFO) </p>
<p> sess_pipeline – Session Pipeline (INFO) </p>
<p> sess_readahead – Session Read Ahead (INFO) </p>
<p> sess_herd – Session herd (DIAG) </p>
<p> shm_records – SHM records (DIAG) </p>
<p> shm_writes – SHM writes (DIAG) </p>
<p> shm_flushes – SHM flushes due to overflow (DIAG) </p>
<p> shm_cont – SHM MTX contention (DIAG) </p>
<p> shm_cycles – SHM cycles through buffer (DIAG) </p>
<p> sms_nreq – SMS allocator requests (DIAG) </p>
<p> sms_nobj – SMS outstanding allocations (DIAG) </p>
<p> sms_nbytes – SMS outstanding bytes (DIAG) </p>
<p> sms_balloc – SMS bytes allocated (DIAG) </p>
<p> sms_bfree – SMS bytes freed (DIAG) </p>
<p> backend_req – Backend requests made (INFO) </p>
<p> n_vcl – Number of loaded VCLs in total (INFO) </p>
<p> n_vcl_avail – Number of VCLs available (DIAG) </p>
<p> n_vcl_discard – Number of discarded VCLs (DIAG)</p>
<dt><code>bans – Count of bans (INFO)</code></p>
<dd>Number of all bans in system, including bans superseded by newer bans and bans already checked by the ban-lurker.</p>
<dt><code>bans_completed – Number of bans marked &#8216;completed&#8217; (DIAG)</code></p>
<dd>Number of bans which are no longer active, either because they got checked by the ban-lurker or superseded by newer identical bans.</p>
<dt><code>bans_obj – Number of bans using obj.* (DIAG)</code></p>
<dd>Number of bans which use obj.* variables. These bans can possibly be washed by the ban-lurker.</p>
<dt><code>bans_req – Number of bans using req.* (DIAG)</code></p>
<dd>Number of bans which use req.* variables. These bans can not be washed by the ban-lurker.</p>
<dt><code>bans_added – Bans added (DIAG)</code></p>
<dd>Counter of bans added to ban list.</p>
<dt><code>bans_deleted – Bans deleted (DIAG)</code></p>
<dd>Counter of bans deleted from ban list.</p>
<dt><code>bans_tested – Bans tested against objects (lookup) (DIAG)</code></p>
<dd>Count of how many bans and objects have been tested against each other during hash lookup.</p>
<dt><code>bans_obj_killed – Objects killed by bans (lookup) (DIAG)</code></p>
<dd>Number of objects killed by bans during object lookup.</p>
<dt><code>bans_lurker_tested – Bans tested against objects (lurker) (DIAG)</code></p>
<dd>Count of how many bans and objects have been tested against each other by the ban-lurker.</p>
<dt><code>bans_tests_tested – Ban tests tested against objects (lookup) (DIAG)</code></p>
<dd>Count of how many tests and objects have been tested against each other during lookup. &#8216;ban req.url == foo &amp;&amp; req.http.host == bar&#8217; counts as one in &#8216;bans_tested&#8217; and as two in &#8216;bans_tests_tested&#8217;</p>
<dt><code>bans_lurker_tests_tested – Ban tests tested against objects (lurker) (DIAG)</code></p>
<dd>Count of how many tests and objects have been tested against each other by the ban-lurker. &#8216;ban req.url == foo &amp;&amp; req.http.host == bar&#8217; counts as one in &#8216;bans_tested&#8217; and as two in &#8216;bans_tests_tested&#8217;</p>
<dt><code>bans_lurker_obj_killed – Objects killed by bans (lurker) (DIAG)</code></p>
<dd>Number of objects killed by ban-lurker.</p>
<dt><code>bans_dups – Bans superseded by other bans (DIAG)</code></p>
<dd>Count of bans replaced by later identical bans.</p>
<dt><code>bans_lurker_contention – Lurker gave way for lookup (DIAG)</code></p>
<dd>Number of times the ban-lurker had to wait for lookups.</p>
<dt><code>bans_persisted_bytes – Bytes used by the persisted ban lists (DIAG)</code></p>
<dd>Number of bytes used by the persisted ban lists.</p>
<dt><code>bans_persisted_fragmentation – Extra bytes in persisted ban lists due to fragmentation (DIAG)</code></p>
<dd>Number of extra bytes accumulated through dropped and completed bans in the persistent ban lists. </p>
<p> n_purges – Number of purge operations executed (INFO) </p>
<p> n_obj_purged – Number of purged objects (INFO)</p>
<dt><code>exp_mailed – Number of objects mailed to expiry thread (DIAG)</code></p>
<dd>Number of objects mailed to expiry thread for handling.</p>
<dt><code>exp_received – Number of objects received by expiry thread (DIAG)</code></p>
<dd>Number of objects received by expiry thread for handling. </p>
<p> hcb_nolock – HCB Lookups without lock (DEBUG) </p>
<p> hcb_lock – HCB Lookups with lock (DEBUG) </p>
<p> hcb_insert – HCB Inserts (DEBUG) </p>
<p> esi_errors – ESI parse errors (unlock) (DIAG) </p>
<p> esi_warnings – ESI parse warnings (unlock) (DIAG) </p>
<p> vmods – Loaded VMODs (INFO) </p>
<p> n_gzip – Gzip operations (INFO) </p>
<p> n_gunzip – Gunzip operations (INFO)</p>
<dt><code>vsm_free – Free VSM space (DIAG)</code></p>
<dd>Number of bytes free in the shared memory used to communicate with tools like varnishstat, varnishlog etc.</p>
<dt><code>vsm_used – Used VSM space (DIAG)</code></p>
<dd>Number of bytes used in the shared memory used to communicate with tools like varnishstat, varnishlog etc.</p>
<dt><code>vsm_cooling – Cooling VSM space (DEBUG)</code></p>
<dd>Number of bytes which will soon (max 1 minute) be freed in the shared memory used to communicate with tools like varnishstat, varnishlog etc.</p>
<dt><code>vsm_overflow – Overflow VSM space (DIAG)</code></p>
<dd>Number of bytes which does not fit in the shared memory used to communicate with tools like varnishstat, varnishlog etc.</p>
<dt><code>vsm_overflowed – Overflowed VSM space (DIAG)</code></p>
<dd>Total number of bytes which did not fit in the shared memory used to communicate with tools like varnishstat, varnishlog etc.</dl>
<h2>Lock Counters</h2>
<p>creat – Created locks (DEBUG) </p>
<p> destroy – Destroyed locks (DEBUG) </p>
<p> locks – Lock Operations (DEBUG)</p>
<h2>Per Malloc Storage Counters</h2>
<p>c_req – Allocator requests (INFO) </p>
<p> c_fail – Allocator failures (INFO) </p>
<p> c_bytes – Bytes allocated (INFO) </p>
<p> c_freed – Bytes freed (INFO) </p>
<p> g_alloc – Allocations outstanding (INFO) </p>
<p> g_bytes – Bytes outstanding (INFO) </p>
<p> g_space – Bytes available (INFO)</p>
<h2>Per File Storage Counters</h2>
<p>c_req – Allocator requests (INFO) </p>
<p> c_fail – Allocator failures (INFO) </p>
<p> c_bytes – Bytes allocated (INFO) </p>
<p> c_freed – Bytes freed (INFO) </p>
<p> g_alloc – Allocations outstanding (INFO) </p>
<p> g_bytes – Bytes outstanding (INFO) </p>
<p> g_space – Bytes available (INFO) </p>
<p> g_smf – N struct smf (INFO) </p>
<p> g_smf_frag – N small free smf (INFO) </p>
<p> g_smf_large – N large free smf (INFO)</p>
<h2>Per Backend Counters</h2>
<p>vcls – VCL references (DEBUG) </p>
<p> happy – Happy health probes (INFO)</p>
<dl>
<dt><code>bereq_hdrbytes – Request header bytes (INFO)</code></p>
<dd>Total backend request header bytes sent</p>
<dt><code>bereq_bodybytes – Request body bytes (INFO)</code></p>
<dd>Total backend request body bytes sent</p>
<dt><code>beresp_hdrbytes – Response header bytes (INFO)</code></p>
<dd>Total backend response header bytes received</p>
<dt><code>beresp_bodybytes – Response body bytes (INFO)</code></p>
<dd>Total backend response body bytes received</p>
<dt><code>pipe_hdrbytes – Pipe request header bytes (INFO)</code></p>
<dd>Total request bytes sent for piped sessions</p>
<dt><code>pipe_out – Piped bytes to backend (INFO)</code></p>
<dd>Total number of bytes forwarded to backend in pipe sessions</p>
<dt><code>pipe_in – Piped bytes from backend (INFO)</code></p>
<dd>Total number of bytes forwarded from backend in pipe sessions </p>
</dl>
