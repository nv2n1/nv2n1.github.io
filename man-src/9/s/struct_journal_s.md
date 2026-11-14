---
title: "struct_journal_s(9)"
name: "struct_journal_s"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_journal_s/"
description: "struct_journal_s – The journal_s type is the concrete type associated with journal_t."
---

<p>struct_journal_s &#8211; The journal_s type is the concrete type associated with journal_t.</p>
<h2>Synopsis</h2>
<pre><code>struct journal_s {
    unsigned long j_flags;
    int j_errno;
    struct buffer_head *j_sb_buffer;
    journal_superblock_t *j_superblock;
    int j_format_version;
    rwlock_t j_state_lock;
    int j_barrier_count;
    struct mutex j_barrier;
    transaction_t *j_running_transaction;
    transaction_t *j_committing_transaction;
    transaction_t *j_checkpoint_transactions;
    wait_queue_head_t j_wait_transaction_locked;
    wait_queue_head_t j_wait_done_commit;
    wait_queue_head_t j_wait_commit;
    wait_queue_head_t j_wait_updates;
    wait_queue_head_t j_wait_reserved;
    struct mutex j_checkpoint_mutex;
    unsigned long j_head;
    unsigned long j_tail;
    unsigned long j_free;
    unsigned long j_first;
    unsigned long j_last;
    struct block_device *j_dev;
    int j_blocksize;
    unsigned long long j_blk_offset;
    struct block_device *j_fs_dev;
    unsigned int j_maxlen;
    atomic_t j_reserved_credits;
    spinlock_t j_list_lock;
    struct inode *j_inode;
    tid_t j_tail_sequence;
    tid_t j_transaction_sequence;
    tid_t j_commit_sequence;
    tid_t j_commit_request;
    __u8 j_uuid[16];
    struct task_struct *j_task;
    int j_max_transaction_buffers;
    unsigned long j_commit_interval;
    struct timer_list j_commit_timer;
    spinlock_t j_revoke_lock;
    struct jbd2_revoke_table_s *j_revoke;
    struct jbd2_revoke_table_s *j_revoke_table[2];
    struct buffer_head **j_wbuf;
    int j_wbufsize;
    pid_t j_last_sync_writer;
    spinlock_t j_history_lock;
    struct proc_dir_entry *j_proc_entry;
    struct transaction_stats_s j_stats;
    void *j_private;
#ifdef CONFIG_DEBUG_LOCK_ALLOC
    struct lockdep_map j_trans_commit_map;
#endif
};</code></pre>
<h2>Members</h2>
<p>j_flags</p>
<dl>
<dd>General journaling state flags</dl>
<p> j_errno</p>
<dl>
<dd>Is there an outstanding uncleared error on the journal (from a prior abort)?</dl>
<p> j_sb_buffer</p>
<dl>
<dd>First part of superblock buffer</dl>
<p> j_superblock</p>
<dl>
<dd>Second part of superblock buffer</dl>
<p> j_format_version</p>
<dl>
<dd>Version of the superblock format</dl>
<p> j_state_lock</p>
<dl>
<dd>Protect the various scalars in the journal</dl>
<p> j_barrier_count</p>
<dl>
<dd>Number of processes waiting to create a barrier lock</dl>
<p> j_barrier</p>
<dl>
<dd>The barrier lock itself</dl>
<p> j_running_transaction</p>
<dl>
<dd>The current running transaction..</dl>
<p> j_committing_transaction</p>
<dl>
<dd>the transaction we are pushing to disk</dl>
<p> j_checkpoint_transactions</p>
<dl>
<dd>a linked circular list of all transactions waiting for checkpointing</dl>
<p> j_wait_transaction_locked</p>
<dl>
<dd>Wait queue for waiting for a locked transaction to start committing, or for a barrier lock to be released</dl>
<p> j_wait_done_commit</p>
<dl>
<dd>Wait queue for waiting for commit to complete</dl>
<p> j_wait_commit</p>
<dl>
<dd>Wait queue to trigger commit</dl>
<p> j_wait_updates</p>
<dl>
<dd>Wait queue to wait for updates to complete</dl>
<p> j_wait_reserved</p>
<dl>
<dd>Wait queue to wait for reserved buffer credits to drop</dl>
<p> j_checkpoint_mutex</p>
<dl>
<dd>Mutex for locking against concurrent checkpoints</dl>
<p> j_head</p>
<dl>
<dd>Journal head &#8211; identifies the first unused block in the journal</dl>
<p> j_tail</p>
<dl>
<dd>Journal tail &#8211; identifies the oldest still-used block in the journal.</dl>
<p> j_free</p>
<dl>
<dd>Journal free &#8211; how many free blocks are there in the journal?</dl>
<p> j_first</p>
<dl>
<dd>The block number of the first usable block</dl>
<p> j_last</p>
<dl>
<dd>The block number one beyond the last usable block</dl>
<p> j_dev</p>
<dl>
<dd>Device where we store the journal</dl>
<p> j_blocksize</p>
<dl>
<dd>blocksize for the location where we store the journal.</dl>
<p> j_blk_offset</p>
<dl>
<dd>starting block offset for into the device where we store the journal</dl>
<p> j_fs_dev</p>
<dl>
<dd>Device which holds the client fs. For internal journal this will be equal to j_dev</dl>
<p> j_maxlen</p>
<dl>
<dd>Total maximum capacity of the journal region on disk.</dl>
<p> j_reserved_credits</p>
<dl>
<dd>Number of buffers reserved from the running transaction</dl>
<p> j_list_lock</p>
<dl>
<dd>Protects the buffer lists and internal buffer state.</dl>
<p> j_inode</p>
<dl>
<dd>Optional inode where we store the journal. If present, all journal block numbers are mapped into this inode via <code>bmap</code>.</dl>
<p> j_tail_sequence</p>
<dl>
<dd>Sequence number of the oldest transaction in the log</dl>
<p> j_transaction_sequence</p>
<dl>
<dd>Sequence number of the next transaction to grant</dl>
<p> j_commit_sequence</p>
<dl>
<dd>Sequence number of the most recently committed transaction</dl>
<p> j_commit_request</p>
<dl>
<dd>Sequence number of the most recent transaction wanting commit</dl>
<p> j_uuid[16]</p>
<dl>
<dd>Uuid of client object.</dl>
<p> j_task</p>
<dl>
<dd>Pointer to the current commit thread for this journal</dl>
<p> j_max_transaction_buffers</p>
<dl>
<dd>Maximum number of metadata buffers to allow in a single compound commit transaction</dl>
<p> j_commit_interval</p>
<dl>
<dd>What is the maximum transaction lifetime before we begin a commit?</dl>
<p> j_commit_timer</p>
<dl>
<dd>The timer used to wakeup the commit thread</dl>
<p> j_revoke_lock</p>
<dl>
<dd>Protect the revoke table</dl>
<p> j_revoke</p>
<dl>
<dd>The revoke table &#8211; maintains the list of revoked blocks in the current transaction.</dl>
<p> j_revoke_table[2]</p>
<dl>
<dd>alternate revoke tables for j_revoke</dl>
<p> j_wbuf</p>
<dl>
<dd>array of buffer_heads for jbd2_journal_commit_transaction</dl>
<p> j_wbufsize</p>
<dl>
<dd>maximum number of buffer_heads allowed in j_wbuf, the number that will fit in j_blocksize</dl>
<p> j_last_sync_writer</p>
<dl>
<dd>most recent pid which did a synchronous write</dl>
<p> j_history_lock</p>
<dl>
<dd>Protect the transactions statistics history</dl>
<p> j_proc_entry</p>
<dl>
<dd>procfs entry for the jbd statistics directory</dl>
<p> j_stats</p>
<dl>
<dd>Overall statistics</dl>
<p> j_private</p>
<dl>
<dd>An opaque pointer to fs-private information.</dl>
<p> j_trans_commit_map</p>
<dl>
<dd>Lockdep entity to track transaction commit dependencies</dl>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
