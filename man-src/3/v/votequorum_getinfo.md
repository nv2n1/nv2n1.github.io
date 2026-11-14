---
title: "votequorum_getinfo(3)"
name: "votequorum_getinfo"
section: "3"
letter: "v"
url: "/docs/linux/man/3-votequorum_getinfo/"
description: "votequorum_getinfo – Get information about the VoteQuorum service"
---

<p>votequorum_getinfo &#8211; Get information about the VoteQuorum service</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/votequorum.h&gt;
int votequorum_getinfo(votequorum_handle_t *handle, unsigned int nodeid, struct votequorum_info *info);</code></pre>
<h2>Description</h2>
<p>The <code>votequorum_getinfo</code> function is used to get information about the voting system and its nodes. The <i>nodeid</i> argument indicates which node information should be stored in the votequorum_info structure. The votequorum_info structure is defined as follows: </p>
<pre><code>struct votequorum_info {
    unsigned int node_id;
    unsigned int node_state;
    unsigned int node_votes;
    unsigned int node_expected_votes;
    unsigned int highest_expected;
    unsigned int total_votes;
    unsigned int quorum;
    unsigned int flags;
    unsigned int qdevice_votes;
    char qdevice_name[VOTEQUORUM_QDEVICE_MAX_NAME_LEN];
};

The node_state is defined as :

#define VOTEQUORUM_NODESTATE_MEMBER 1
#define VOTEQUORUM_NODESTATE_DEAD 2
#define VOTEQUORUM_NODESTATE_LEAVING 3

    The flags are defined as:

#define VOTEQUORUM_INFO_TWONODE 1
#define VOTEQUORUM_INFO_QUORATE 2
#define VOTEQUORUM_INFO_WAIT_FOR_ALL 4
#define VOTEQUORUM_INFO_LAST_MAN_STANDING 8
#define VOTEQUORUM_INFO_AUTO_TIE_BREAKER 16
#define VOTEQUORUM_INFO_ALLOW_DOWNSCALE 32
#define VOTEQUORUM_INFO_QDEVICE_REGISTERED 64
#define VOTEQUORUM_INFO_QDEVICE_ALIVE 128
#define VOTEQUORUM_INFO_QDEVICE_CAST_VOTE 256
#define VOTEQUORUM_INFO_QDEVICE_MASTER_WINS 512</code></pre>
<p> The members starting node_ hold information specific to the requested nodeid, the other are general to the voting system.</p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise a generic error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-votequorum_initialize/">votequorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_finalize/">votequorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstart/">votequorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstop/">votequorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_fd_get/">votequorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_dispatch/">votequorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_set/">votequorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_get/">votequorum_context_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setexpected/">votequorum_setexpected</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setvotes/">votequorum_setvotes</a></code>(3) </p>
