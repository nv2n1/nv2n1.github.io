---
title: "tm(3)"
name: "tm"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tm/"
description: "tm_init, tm_nodeinfo, tm_poll, tm_notify, tm_spawn, tm_kill, tm_obit, tm_taskinfo, tm_atnode, tm_rescinfo, tm_publish, tm_subscribe, tm_finalize – task management API"
---

<p>tm_init, tm_nodeinfo, tm_poll, tm_notify, tm_spawn, tm_kill, tm_obit, tm_taskinfo, tm_atnode, tm_rescinfo, tm_publish, tm_subscribe, tm_finalize &#8211; task management API</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tm.h&gt;
int tm_init(info, roots) void *info;
struct tm_roots *roots;
int tm_nodeinfo(list, nnodes)
tm_node_id ***list;
int *nnodes;
int tm_poll(poll_event, result_event, wait, tm_errno)
tm_event_t poll_event;
tm_event_t *result_event;
int wait;
int *tm_errno;
int tm_notify(tm_signal)
int tm_signal;
int tm_spawn(argc, argv, envp, where, tid, event)
int argc;
char **argv;
char **envp;
tm_node_id where;
tm_task_id *tid;
tm_event_t *event;
int tm_kill(tid, sig, event)
tm_task_id tid;
int sig;
tm_event_t event;
int tm_obit(tid, obitval, event)
tm_task_id tid;
int *obitval;
tm_event_t event;
int tm_taskinfo(node, tid_list, list_size, ntasks, event)
tm_node_id node;
tm_task_id *tid_list;
int list_size;
int *ntasks;
tm_event_t event;
int tm_atnode(tid, node)
tm_task_id tid;
tm_node_id *node;
int tm_rescinfo(node, resource, len, event)
tm_node_id node;
char *resource;
int len;
tm_event_t event;
int tm_publish(name, info, len, event)
char *name;
void *info;
int len;
tm_event_t event;
int tm_subscribe(tid, name, info, len, info_len, event)
tm_task_id tid;
char *name;
void *info;
int len;
int *info_len;
tm_event_t event;</code></pre>
<pre><code>int tm_finalize()</code></pre>
<h2>Description</h2>
<p>These functions provide a partial implementation of the task management interface part of the PSCHED API. In PBS, MOM provides the task manager functions. This library opens a tcp socket to the MOM running on the local host and sends and receives messages. The PSCHED Task Management API description used to create this library was commited to paper on Novermber 15, 1996 and was given the version number 0.1. Changes may have taken place since that time which are not reflected in this library. The API description uses several data types that it purposefully does not define. This was done so an implementaion would not be confined in the way it was written. For this specific work, the definitions follow: struct tm_roots {<br />
    tm_task_id tm_me;<br />
    tm_task_id tm_parent;<br />
    int tm_nnodes;<br />
    int tm_ntasks;<br />
    int tm_taskpoolid;<br />
    tm_task_id *tm_tasklist;<br />
}; There are a number of error values defined as well: TM_SUCCESS, TM_ESYSTEM, TM_ENOEVENT, TM_ENOTCONNECTED, TM_EUNKNOWNCMD, TM_ENOTIMPLEMENTED, TM_EBADENVIRONMENT, TM_ENOTFOUND. <code>tm_init()</code> initializes the library by opening a socket to the MOM on the local host and sending a TM_INIT message, then waiting for the reply. The <i>info</i> paramenter has no use and is included to conform with the PSCHED document. The <i>roots</i> pointer will contain valid data after the function returns and has the following structure: </p>
<pre><code>struct tm_roots {
    tm_task_id tm_me;
    tm_task_id tm_parent;
    int tm_nnodes;
    int tm_ntasks;
    int tm_taskpoolid;
    tm_task_id *tm_tasklist;
};</code></pre>
<dl>
<dt>tm_me</p>
<dd>The task id of this calling task.</p>
<dt>tm_parent</p>
<dd>The task id of the task which spawned this task or TM_NULL_TASK if the calling task is the initial task started by PBS.</p>
<dt>tm_nnodes</p>
<dd>The number of nodes allocated to the job.</p>
<dt>tm_ntasks</p>
<dd>This will always be 0 for PBS.</p>
<dt>tm_taskpoolid</p>
<dd>PBS does not support task pools so this will always be -1.</p>
<dt>tm_tasklist</p>
<dd>This will be NULL for PBS.</dl>
<p> The <i>tm_ntasks</i>, <i>tm_taskpoolid</i> and <i>tm_tasklist</i> fields are not filled with data specified by the PSCHED document. PBS does not support task pools and, at this time, does not return information about current running tasks from <code>tm_init.</code> There is a separate call to get information for current running tasks called <code>tm_taskinfo</code> which is described below. The return value from <code>tm_init</code> be TM_SUCCESS if the library initialization was successful, or an error return otherwise. <code>tm_nodeinfo()</code> places a pointer to a malloc&#8217;ed array of tm_node_id&#8217;s in the pointer pointed at by <i>list</i>. The order of the tm_node_id&#8217;s in <i>list</i> is the same as that specified to MOM in the &quot;exec_host&quot; attribute. The int pointed to by <i>nnodes</i> contains the number of nodes allocated to the job. This is information that is returned during initialization and does not require communication with MOM. If <code>tm_init</code> has not been called, TM_ESYSTEM is returned, otherwise TM_SUCCESS is returned. <code>tm_poll()</code> is the function which will retrieve information about the task management system to locations specified when other routines request an action take place. The bookkeeping for this is done by generating an <i>event</i> for each action. When the task manager (MOM) sends a message that an action is complete, the event is reported by <code>tm_poll</code> and information is placed where the caller requested it. The argument <i>poll_event</i> is meant to be used to request a specific event. This implementation does not use it and it must be set to TM_NULL_EVENT or an error is returned. Upon return, the argument <i>result_event</i> will contain a valid event number or TM_ERROR_EVENT on error. If <i>wait</i> is zero and there are no events to report, <i>result_event</i> is set to TM_NULL_EVENT. If <i>wait</i> is non-zero an there are no events to report, the function will block waiting for an event. If no local error takes place, TM_SUCCESS is returned. If an error is reported by MOM for an event, then the argument <i>tm_errno</i> will be set to an error code. <code>tm_notify()</code> is described in the PSCHED documentation, but is not implemented for PBS yet. It will return TM_ENOTIMPLEMENTED. <code>tm_spawn()</code> sends a message to MOM to start a new task. The node id of the host to run the task is given by <i>where</i>. The parameters <i>argc</i>, <i>argv</i> and <i>envp</i> specify the program to run and its arguments and environment very much like <code>exec().</code> The full path of the program executable must be given by <i>argv[0]</i> and the number of elements in the argv array is given by <i>argc</i>. The array <i>envp</i> is NULL terminated. The argument <i>event</i> points to a tm_event_t variable which is filled in with an event number. When this event is returned by <code>tm_poll ,</code> the tm_task_id pointed to by <i>tid</i> will contain the task id of the newly created task. In addition, the tid is available to the process in the <code>PBS_TASKNUM</code> environment variable. Similarly, the node number is in the <code>PBS_NODENUM</code> variable and the cpu number is in the <code>PBS_VNODENUM</code> variable. <code>tm_kill()</code> sends a signal specified by <i>sig</i> to the task <i>tid</i> and puts an event number in the tm_event_t pointed to by <i>event</i>. <code>tm_obit()</code> creates an event which will be reported when the task <i>tid</i> exits. The int pointed to by <i>obitval</i> will contain the exit value of the task when the event is reported. <code>tm_taskinfo()</code> returns the list of tasks running on the node specified by <i>node</i>. The PSCHED documentation mentions a special ability to retrieve all tasks running in the job. This is not supported by PBS. The argument <i>tid_list</i> points to an array of tm_task_id&#8217;s which contains <i>list_size</i> elements. Upon return, <i>event</i> will contain an event number. When this event is polled, the int pointed to by <i>ntasks</i> will contain the number of tasks running on the node and the array will be filled in with tm_task_id&#8217;s. If <i>ntasks</i> is greater than <i>list_size</i>, only <i>list_size</i> tasks will be returned. <code>tm_atnode()</code> will place the node id where the task <i>tid</i> exists in the tm_node_id pointed to by <i>node</i>. <code>tm_rescinfo()</code> makes a request for a string specifying the resources available on a node given by the argument <i>node</i>. The string is returned in the buffer pointed to by <i>resource</i> and is terminated by a NUL character unless the number of characters of information is greater than specified by <i>len</i>. The resource string PBS returns is formated as follows: A space separated set of strings from the <code>uname</code> system call followed by a colon (:). The order of the strings is <code>sysname,</code> <code>nodename,</code> <code>release,</code> <code>version,</code> <code>machine.</code> A comma spearated set of strings giving the components of the &quot;Resource_List&quot; attribute of the job. Each component has the resource name, an equal sign, and the limit value. For example, a return for a task running on an SGI workstation might look like: IRIX golum 6.2 03131015 IP22:cput=20:00,mem=400kb <code>tm_publish()</code> causes <i>len</i> bytes of information pointed at by <i>info</i> to be sent to the local MOM to be saved under the name given by <i>name</i>. <code>tm_subscribe()</code> returns a copy of the information named by <i>name</i> for the task given by <i>tid</i>. The argument <i>info</i> points to a buffer of size <i>len</i> where the information will be returned. The argument <i>info_len</i> will be set with the size of the published data. If this is larger than the supplied buffer, the data will have been truncated. <code>tm_finalize()</code> may be called to free any memory in use by the library and close the connection to MOM.</p>
<h2>See Also</h2>
<p><code>pbs_mom,</code> <code>PSCHED: An API for Parallel Job/Resource Managment,</code> <code><a rel="nofollow" href="http://parallel.nas.nasa.gov/Psched/psched-api-report.ps">http://parallel.nas.nasa.gov/Psched/psched-api-report.ps</a></code> </p>
