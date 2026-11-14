---
title: "libiperf(3)"
name: "libiperf"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libiperf/"
---

<h2>NAME</h2>

 libiperf - API for iperf3 network throughput tester 

<h2>SYNOPSIS</h2>

 #include &lt;iperf_api.h&gt; 
 -liperf 

<h2>DESCRIPTION</h2>

 

 Libiperf gives you access to all the functionality of the iperf3 network testing tool. You can build it directly into your own program, instead of having to run it as a shell command. 

<h2>CALLS</h2>

 Initialization / termination: <pre><code>
struct iperf_test *iperf_new_test();
int iperf_defaults(struct iperf_test *t);
void iperf_free_test(struct iperf_test *t);
</code></pre> Setting test parameters: 
void iperf_set_test_role(struct iperf_test *pt, char role);
void iperf_set_test_bind_address(struct iperf_test *t, char *bind_address);
void iperf_set_test_server_hostname(struct iperf_test *t, char *server_host);
void iperf_set_test_server_port(struct iperf_test *t, int server_port);
void iperf_set_test_duration(struct iperf_test *t, int duration);
void iperf_set_test_blksize(struct iperf_test *t, int blksize);
void iperf_set_test_num_streams(struct iperf_test *t, int num_streams);
void iperf_set_test_json_output(struct iperf_test *t, int json_output);
int iperf_has_zerocopy(void);
void iperf_set_test_zerocopy(struct iperf_test *t, int zerocopy);
 Running a test: 
int iperf_run_client(struct iperf_test *);
int iperf_run_server(struct iperf_test *);
void iperf_test_reset(struct iperf_test *);
 Output: 
FILE *iperf_get_test_outfile(struct iperf_test *);
char *iperf_get_test_json_output_string(struct iperf_test *);
 Error reporting: 
void iperf_err(struct iperf_test *t, const char *format, ...);
char *iperf_strerror(int);
extern int i_errno;
 This is not a complete list of the available calls. See the include file for more. 

<h2>EXAMPLES</h2>

 Here's some sample code that runs an iperf client: 
struct iperf_test *test;
test = iperf_new_test();
if (test == NULL) {
        fprintf( stderr, "%s: failed to create test, argv0 );
        exit( EXIT_FAILURE );
}
iperf_defaults(test);
iperf_set_test_role(test, 'c');
iperf_set_test_server_hostname(test, host);
iperf_set_test_server_port(test, port);
if (iperf_run_client(test) &lt; 0) {
        fprintf( stderr, "%s: error - %s, argv0, iperf_strerror( i_errno ) );
        exit( EXIT_FAILURE );
}
iperf_free_test(test);
 And here's a server: <pre><code>
struct iperf_test *test;
test = iperf_new_test();
if (test == NULL) {
        fprintf( stderr, "%s: failed to create test, argv0 );
        exit( EXIT_FAILURE );
}
iperf_defaults(test);
iperf_set_test_role(test, 's');
iperf_set_test_server_port(test, port);
for (;;) {
    if (iperf_run_server(test) &lt; 0)
        fprintf(stderr, "%s: error - %sn", argv0, iperf_strerror(i_errn o));
    iperf_reset_test(test);
}
iperf_free_test(test);
</code></pre> These are not complete programs, just excerpts. The full runnable source code can be found in the examples subdirectory of the iperf3 source tree. 

<h2>AUTHORS</h2>

 A list of the contributors to iperf3 can be found within the documentation located at <a rel="nofollow" HREF="http://software.es.net/iperf/dev.html#authors.">http://software.es.net/iperf/dev.html#authors.</a> 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-iperf3/">iperf3</a>(1), <a rel="nofollow" HREF="http://software.es.net/iperf/">http://software.es.net/iperf/</a> 

<h2>Index</h2>


