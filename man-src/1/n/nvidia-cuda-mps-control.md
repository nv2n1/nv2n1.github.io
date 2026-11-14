---
title: "nvidia-cuda-mps-control(1)"
name: "nvidia-cuda-mps-control"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvidia-cuda-mps-control/"
description: "nvidia-cuda-mps-control – NVIDIA CUDA Multi Process Service management program"
---

<h2 class="name">NAME</h2>
<p> nvidia-cuda-mps-control &#8211; NVIDIA CUDA Multi Process Service management program </p>
<h2>SYNOPSIS</h2>
<p> <code>nvidia-cuda-mps-control</code> [<code>-d | -f</code>]</p>
<h2>DESCRIPTION</h2>
<p> MPS is a runtime service designed to let multiple MPI processes using CUDA to run concurrently in a way that&#8217;s transparent to the MPI program. A CUDA program runs in MPS mode if the MPS control daemon is running on the system. </p>
<p> When CUDA is first initialized in a program, the CUDA driver attempts to connect to the MPS control daemon. If the connection attempt fails, the program continues to run as it normally would without MPS. If however, the connection attempt to the control daemon succeeds, the CUDA driver then requests the daemon to start an MPS server on its behalf. If there&#8217;s an MPS server already running, and the user id of that server process matches that of the requesting client process, the control daemon simply notifies the client process of it, which then proceeds to connect to the server. If there&#8217;s no MPS server already running on the system, the control daemon launches an MPS server with the same user id (UID) as that of the requesting client process. If there&#8217;s an MPS server already running, but with a different user id than that of the client process, the control daemon requests the existing server to shutdown as soon as all its clients are done. Once the existing server has terminated, the control daemon launches a new server with the user id same as that of the queued client process. </p>
<p> The MPS server creates the shared GPU context, and manages its clients. An MPS server can support a finite amount of CUDA contexts determined by the hardware architecture it is running on. For compute capability SM 3.5 through SM 6.0 the limit is 16 clients per GPU at a time. Compute capability SM 7.0 has a limit of 48. MPS is transparent to CUDA programs, with all the complexity of communication between the client process, the server and the control daemon hidden within the driver binaries. </p>
<p> Currently, CUDA MPS is available on 64-bit Linux only, requires a device that supports Unified Virtual Address (UVA) and has compute capability SM 3.5 or higher. Applications requiring pre-CUDA 4.0 APIs are not supported under CUDA MPS. Certain capabilities are only available starting with compute capability SM 7.0.</p>
<h2>OPTIONS</h2>
<h3>-d</h3>
<p> Start the MPS control daemon in background mode, assuming the user has enough privilege (e.g. root). Parent process exits when control daemon started listening for client connections.</p>
<h3>-f</h3>
<p> Start the MPS control daemon in foreground mode, assuming the user has enough privilege (e.g. root). The debug messages are sent to standard output.</p>
<h3>-h, &#8211;help</h3>
<p> Print a help message.</p>
<h3>&lt;no arguments&gt;</h3>
<p> Start the front-end management user interface to the MPS control daemon, which needs to be started first. The front-end UI keeps reading commands from stdin until EOF. Commands are separated by the newline character. If an invalid command is issued and rejected, an error message will be printed to stdout. The exit status of the front-end UI is zero if communication with the daemon is successful. A non-zero value is returned if the daemon is not found or connection to the daemon is broken unexpectedly. See the &quot;quit&quot; command below for more information about the exit status. </p>
<p> Commands supported by the MPS control daemon:</p>
<dl>
<dt><code>get_server_list</code></p>
<dd> Print out a list of PIDs of all MPS servers.</p>
<dt><code>start_server</code> <code>-uid</code> <i>UID</i></p>
<dd> Start a new MPS server for the specified user (<i>UID</i>).</p>
<dt><code>shutdown_server</code> <i>PID</i> [<code>-f</code>]</p>
<dd> Shutdown the MPS server with given <i>PID</i>. The MPS server will not accept any new client connections and it exits when all current clients disconnect. <code>-f</code> is forced immediate shutdown. If a client launches a faulty kernel that runs forever, a forced shutdown of the MPS server may be required, since the MPS server creates and issues GPU work on behalf of its clients.</p>
<dt><code>get_client_list</code> <i>PID</i></p>
<dd> Print out a list of PIDs of all clients connected to the MPS server with given <i>PID</i>.</p>
<dt><code>quit</code> [<code>-t</code> <i>TIMEOUT</i>]</p>
<dd> Shutdown the MPS control daemon process and all MPS servers. The MPS control daemon stops accepting new clients while waiting for current MPS servers and MPS clients to finish. If <i>TIMEOUT</i> is specified (in seconds), the daemon will force MPS servers to shutdown if they are still running after <i>TIMEOUT</i> seconds. </p>
<p> This command is synchronous. The front-end UI waits for the daemon to shutdown, then returns the daemon&#8217;s exit status. The exit status is zero iff all MPS servers have exited gracefully.</p>
<dt>Commands available to Volta MPS control daemon:</p>
<dd>
<dt><code>get_device_client_list</code> <i>PID</i></p>
<dd> List the devices and PIDs of client applications that enumerated this device. It optionally takes the server instance PID.</p>
<dt><code>set_default_active_thread_percentage</code> <i>percentage</i></p>
<dd> Set the default active thread percentage for MPS servers. If there is already a server spawned, this command will only affect the next server. The set value is lost if a quit command is executed. The default is 100.</p>
<dt><code>get_default_active_thread_percentage</code></p>
<dd> Query the current default available thread percentage.</p>
<dt><code>set_active_thread_percentage</code> <i>PID</i> <i>percentage</i></p>
<dd> Set the active thread percentage for the MPS server instance of the given PID. All clients created with that server afterwards will observe the new limit. Existing clients are not affected.</p>
<dt><code>get_active_thread_percentage</code> <i>PID</i></p>
<dd> Query the current available thread percentage of the MPS server instance of the given PID.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>CUDA_MPS_PIPE_DIRECTORY</code></p>
<dd> Specify the directory that contains the named pipes and UNIX domain sockets used for communication among the MPS control, MPS server, and MPS clients. The value of this environment variable should be consistent in the MPS control daemon and all MPS client processes. Default directory is /tmp/nvidia-mps</p>
<dt><code>CUDA_MPS_LOG_DIRECTORY</code></p>
<dd> Specify the directory that contains the MPS log files. This variable is used by the MPS control daemon only. Default directory is /var/log/nvidia-mps</dl>
<h2>FILES</h2>
<p> Log files created by the MPS control daemon in the specified directory</p>
<dl>
<dt><code>control.log</code></p>
<dd> Record startup and shutdown of MPS control daemon, user commands issued with their results, and status of MPS servers.</p>
<dt><code>server.log</code></p>
<dd> Record startup and shutdown of MPS servers, and status of MPS clients. </p>
</dl>
<h2>Index</h2>
