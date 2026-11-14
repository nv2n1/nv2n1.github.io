---
title: "tevent_data(3)"
name: "tevent_data"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tevent_data/"
---

tevent_data - Chapter 3: Accessing data

<h2>Accessing data with tevent</h2>

A tevent request is (usually) created together with a structure for storing the data necessary for an asynchronous computation. For these private data, tevent library uses void (generic) pointers, therefore any data type can be very simply pointed at. However, this attitude requires clear and guaranteed knowledge of the data type that will be handled, in advance. Private data can be of 2 types: connected with a request itself or given as an individual argument to a callback. It is necessary to differentiate these types, because there is a slightly different method of data access for each. There are two possibilities how to access data that is given as an argument directly to a callback. The difference lies in the pointer that is returned. In one case it is the data type specified in the function’s argument, in another void* is returned. 

 

 <pre>void tevent_req_callback_data (struct tevent_req *req, #type)
void tevent_req_callback_data_void (struct tevent_req *req)</pre>To obtain data that are strictly bound to a request, this function is the only direct procedure. 

 

 <pre>void *tevent_req_data (struct tevent_req *req, #type)</pre>Example with both calls which differs between private data within tevent request and data handed over as an argument. 

 

 <pre>#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;tevent.h&gt;
struct foo_state {
 int x;
};
struct testA {
 int y;
};
static void foo_done(struct tevent_req *req) {
 // a-&gt;x contains 10 since it came from foo_send
 struct foo_state *a = tevent_req_data(req, struct foo_state);
 // b-&gt;y contains 9 since it came from run
 struct testA *b = tevent_req_callback_data(req, struct testA);
 // c-&gt;y contains 9 since it came from run we just used a different way
 // of getting it.
 struct testA *c = (struct testA *)tevent_req_callback_data_void(req);
 printf(&quot;a-&gt;x: %d, a-&gt;x);
 printf(&quot;b-&gt;y: %d, b-&gt;y);
 printf(&quot;c-&gt;y: %d, c-&gt;y);
}
struct tevent_req * foo_send(TALLOC_CTX *mem_ctx, struct tevent_context *event_ctx) {
printf(&quot;_send);
struct tevent_req *req;
struct foo_state *state;
req = tevent_req_create(event_ctx, &amp;state, struct foo_state);
state-&gt;x = 10;
return req;
}
static void run(struct tevent_context *ev, struct tevent_timer *te,
 struct timeval current_time, void *private_data) {
 struct tevent_req *req;
 struct testA *tmp = talloc(ev, struct testA);
 // Note that we did not use the private data passed in
 tmp-&gt;y = 9;
 req = foo_send(ev, ev);
 tevent_req_set_callback(req, foo_done, tmp);
 tevent_req_done(req);
}
int main (int argc, char **argv) {
 struct tevent_context *event_ctx;
 struct testA *data;
 TALLOC_CTX *mem_ctx;
 struct tevent_timer *time_event;
 mem_ctx = talloc_new(NULL); //parent
 if (mem_ctx == NULL)
 return EXIT_FAILURE;
 event_ctx = tevent_context_init(mem_ctx);
 if (event_ctx == NULL)
 return EXIT_FAILURE;
 data = talloc(mem_ctx, struct testA);
 data-&gt;y = 11;
 time_event = tevent_add_timer(event_ctx,
 mem_ctx,
 tevent_timeval_current(),
 run,
 data);
 if (time_event == NULL) {
 fprintf(stderr, &quot; FAILED);
 return EXIT_FAILURE;
 }
 tevent_loop_once(event_ctx);
 talloc_free(mem_ctx);
 printf(&quot;Quit);
 return EXIT_SUCCESS;
}</pre>Output of this example is: 

 

 <pre>a-&gt;x: 10
b-&gt;y: 9
c-&gt;y: 9</pre>&nbsp;<wbr>
