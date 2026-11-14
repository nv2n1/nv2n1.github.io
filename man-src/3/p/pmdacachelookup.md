---
title: "pmdacachelookup(3)"
name: "pmdacachelookup"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdacachelookup/"
description: "pmdaCacheStore, pmdaCacheStoreKey, pmdaCacheLookup, pmdaCacheLookupName, pmdaCacheLookupKey, pmdaCacheOp, pmdaCachePurge, pmdaCacheResize – manage a cache of instance domain information for a PMDA"
---

<p><code>pmdaCacheStore</code>, <code>pmdaCacheStoreKey</code>, <code>pmdaCacheLookup</code>, <code>pmdaCacheLookupName</code>, <code>pmdaCacheLookupKey</code>, <code>pmdaCacheOp</code>, <code>pmdaCachePurge</code>, <code>pmdaCacheResize</code> &#8211; manage a cache of instance domain information for a PMDA</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaCacheStore(pmInDom </code><i>indom</i>, int <i>flags</i>, const char&nbsp;<wbr>*<i>name</i>, void&nbsp;<wbr>*<i>private</i>); </p>
<p> int pmdaCacheStoreKey(pmInDom <i>indom</i>, int <i>flags</i>, const char&nbsp;<wbr>*<i>name</i>, int&nbsp;<wbr><i>keylen</i>, const void&nbsp;<wbr>*<i>key</i>, void&nbsp;<wbr>*<i>private</i>); </p>
<p> int pmdaCacheLookup(pmInDom <i>indom</i>, int <i>inst</i>, char **<i>name</i>, void&nbsp;<wbr>**<i>private</i>); </p>
<p> int pmdaCacheLookupName(pmInDom <i>indom</i>, const char *<i>name</i>, int&nbsp;<wbr>*<i>inst</i>, void&nbsp;<wbr>**<i>private</i>); </p>
<p> int pmdaCacheLookupKey(pmInDom <i>indom</i>, const char *<i>name</i>, int&nbsp;<wbr><i>keylen</i>, const void&nbsp;<wbr>*<i>key</i>, char **<i>oname</i>, int&nbsp;<wbr>*<i>inst</i>, void&nbsp;<wbr>**<i>private</i>); </p>
<p> int pmdaCacheOp(pmInDom <i>indom</i>, int <i>op</i>); </p>
<p> int pmdaCachePurge(pmInDom <i>indom</i>, time_t <i>recent</i>); </p>
<p> int pmdaCacheResize(pmInDom <i>indom</i>, int <i>maximum</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>The <code>pmdaCache</code> family of routines provide services to support the maintenance of complex instance domains for Performance Co-Pilot PMDAs. There is potentially one cache of information for each instance domain, and for each instance the cache maintains:</p>
<dl>
<dt>&#8211;</p>
<dd>external instance name (supplied by the PMDA)</p>
<dt>&#8211;</p>
<dd>internal instance identifier (assigned by <code>pmdaCacheStore</code> or calculated from a &#8220;hint&#8221; by <code>pmdaCacheStoreKey</code>)</p>
<dt>&#8211;</p>
<dd>state, where <code>active</code> instances are visible and part of the current instance domain, and <code>inactive</code> instances are hidden, but not forgotten; <code>pmdaCacheStore</code> or <code>pmdaCacheStoreKey</code> may be used to change the state of an instance</p>
<dt>&#8211;</p>
<dd>an optional opaque pointer to data that is associated with the instance, but maintained by the PMDA</p>
<dt>&#8211;</p>
<dd>an optional opaque key that is used as a &#8220;hint&#8221; to <code>pmdaCacheStoreKey</code> when guessing the initial internal instance identifier</p>
<dt>&#8211;</p>
<dd>the last time the cache was saved and the instance had been marked as <code>active</code> at some point since the previous cache load or save operation</dl>
<p> The semantics of a PCP instance domain require a number of rules to be followed, namely:</p>
<dl>
<dt>1.</p>
<dd>Each internal instance identifier must be unique and in the range 0 to 2^31 &#8211; 1. This rule is enforced by the <code>pmdaCache</code> family of routines.</p>
<dt>2.</p>
<dd>The external instance name must be unique. When the instance name contains a space, it is further constrained such that the name to the left of the first space (the short name) must also be unique. Refer to the INSTANCE NAME MATCHING section below. The PMDA must honor this rule, the <code>pmdaCache</code> family of routines will detect attempts to violate this rule.</p>
<dt>3.</p>
<dd>Where an external instance name corresponds to some object or entity, there is an expectation that the association between the name and the object is fixed, e.g. &#8220;/dev/hda&#8221; is always the name of the same disk on a particular system. This rule is perhaps the responsibility of the PMDA, but is often a characteristic of the environment in which the PMDA runs.</p>
<dt>4.</p>
<dd>It is preferable, although not mandatory, for the association between and external instance name and an internal instance identifier to be persistent. This rule is supported by the <code>pmdaCache</code> family of routines.</p>
<dt>5.</p>
<dd>When opaque keys are used, the values of the keys must be unique across all instances within an instance domain. This rule is enforced by the <code>pmdaCache</code> family of routines.</dl>
<p> The visible interface to the cache is oriented towards the PMDA developer who is most concerned about the names of instances, while the details of how the rest of the PCP infrastructure expects the internal instance identifiers to be managed is not relevant. Instances are updated in the cache for instance domain <i>indom</i> by calling <code>pmdaCacheStore</code> or <code>pmdaCacheStoreKey</code> with the external name of the instance passed via <i>name.</i> The opaque pointer <i>private</i> may be used to associate additional data with the entry in the cache; if no such data is required, <i>private</i> should be NULL. Any manipulation of the additional data (including allocation or freeing) is the responsibility of the PMDA caller, as the cache simply maintains the pointer to the data (passed via <i>private</i>). The upper bound for identifiers allocated for any given <i>indom</i> cache can be optionally reduced from the default (2^31 &#8211; 1) to some lesser <i>maximum</i>, using <code>pmdaCacheResize</code>. This <i>maximum</i> will then be persisted and restored in the usual manner, and can thus be associated permanently with a cache once set. This has applications when using these interfaces as general purpose identifier caches, and is less applicable when using them for instance domain caching. For cases where the PMDA developer wishes to influence the allocation of internal instance identifiers, e.g. for instance domains with more than one natural dimension, or where there is a desire to allocate the same instance identifier each time the PMDA is started, even on different hosts, <code>pmdaCacheStoreKey</code> may be used. In this case, an initial &#8220;hint&#8221; for the instance identifier is provided as an opaque key via the first <i>keylen</i> bytes in <i>key</i> (which could be any sort of data, including binary values) else if <i>keylen</i> is less than 1 or <i>key</i> is <code>NULL</code> then <i>name</i> is used as the &#8220;hint&#8221;. The &#8220;hint&#8221; is hashed to produce an initial instance identifier in the range 0 to 2^31 &#8211; 1 (or lesser <i>maximum</i>, if set). If this instance identifier is already allocated, then the value is rehashed. This procedure is repeated until an unallocated instance identifier is found, or <code>pmdaCacheStoreKey</code> gives up and returns <code>PM_ERR_GENERIC</code>. For each instance domain, the &#8220;hint&#8221; must be unique across all instances, else <code>pmdaCacheStoreKey</code> returns <code>PM_ERR_INST</code>. The <i>flags</i> argument controls how the instance should be processed in the cache as follows:</p>
<dl>
<dt>PMDA_CACHE_ADD</p>
<dd>Insert the entry into the cache if it is not already there and mark it <code>active</code>. If the entry is already in the cache mark it <code>active</code>.</p>
<dt>PMDA_CACHE_HIDE</p>
<dd>Mark the entry in the cache as <code>inactive</code>, but remember the details of the association between the external instance name and the internal instance identifier. Entries that are <code>inactive</code> will be hidden from cache traversal via PMDA_CACHE_WALK_NEXT operations, but remain visible to <code>pmdaCacheLookup</code>, <code>pmdaCacheLookupName</code> and <code>pmdaCacheLookupKey</code> requests.</p>
<dt>PMDA_CACHE_CULL</p>
<dd>Remove the entry from the cache.</dl>
<p> On success <code>pmdaCacheStore</code> or <code>pmdaCacheStoreKey</code> will return the internal instance identifier of the associated cache entry. Valid instance identifiers are guaranteed to be unique and non-negative. Failure will be indicated by a negative value (suitable for decoding with <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3)) and most likely PM_ERR_INST to indicate the requested instance is not in the cache, or -EINVAL to indicate a potential violation of the short name uniqueness property (see the INSTANCE NAME MATCHING section below). <code>pmdaCacheLookup</code> is used to search the entries in the cache based on the internal instance identifier <i>inst</i>. On success the return value will be PMDA_CACHE_ACTIVE or PMDA_CACHE_INACTIVE (depending on the <code>active</code> or <code>inactive</code> state of the cache entry), <i>name</i> (if not NULL) and <i>private</i> (if not NULL) will be set to the external instance name and the associate additional data area as provided when the instance was last activated via <code>pmdaCacheStore </code> or <code>pmdaCacheStoreKey</code>. <code>pmdaCacheLookup</code> failure is indicated by a negative return value suitable for decoding with <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3). The <code>pmdaCacheLookup</code> interface is required by the PMDA&#8217;s fetch callback that is registered via <code><a href="/docs/linux/man/3-pmdasetfetchcallback/">pmdaSetFetchCallback</a></code>(3). Here the internal instance identifier is passed to the fetch callback to identifier for which instance a value is required. Typical usage is shown in the code fragment below. <code> </p>
<pre><code>static int
foo_callback(pmdaMetric *mdesc, unsigned int inst, pmAtomValue *atom)
{
    mydata *mdp;
    char *name;
    int sts;

    sts = pmdaCacheLookup(mdesc-&gt;m_desc.indom, inst, &amp;name, (void **)&amp;mdp);
    /*
     * expect sts == PMDA_CACHE_ACTIVE except for cataclysmic events
     * use mdp as required, name may be useful for diagnostics
     */
    ...

pmdaCacheLookupName

is used to search the
entries in the cache based on the external
instance name
name.
On success the return value will be PMDA_CACHE_ACTIVE or PMDA_CACHE_INACTIVE
(depending on the
active

or
inactive

state of the cache entry),
inst

(if not NULL) and
private

(if not NULL)
will be set to the internal instance identifier and the associate additional data
area as provided when the instance was last activated via
pmdaCacheStore

or
pmdaCacheStoreKey.
pmdaCacheLookupName

failure is indicated by a negative return value
suitable for decoding with
pmErrStr(3).
The
pmdaCacheLookupName

interface is useful for PMDAs wishing to update an instance domain based
on the external instance names.
pmdaCacheLookupKey

is used to search the entries in the cache
based on an opaque key (or ``hint'') previously used in a call to
pmdaCacheStoreKey.

The ``hint'' is provided via the first
keylen

bytes in
key.

For symmetry with
pmdaCacheStoreKey,

if
keylen

is less than 1 or
key

is
NULL

then
name

is used as the ``hint'' (although the results will be the same as
calling
pmdaCacheLookupName

in this case).
On success the return value will be PMDA_CACHE_ACTIVE or PMDA_CACHE_INACTIVE
(depending on the
active

or
inactive

state of the cache entry),
oname

(if not NULL),
inst

(if not NULL) and
private

(if not NULL)
will be set to the external instance name, the internal instance
identifier and the associate additional data
area as provided when the instance was last activated via
pmdaCacheStore

or
pmdaCacheStoreKey.
pmdaCacheLookupKey

failure is indicated by a negative return value
suitable for decoding with
pmErrStr(3).
To avoid a persistent cache growing without bound,
pmdaCachePurge

can be used to cull all entries that have
not

been
active

in the last
recent

seconds.
For performance reasons, the time accounting is imprecise and the entries
are timestamped
at the time of the next cache save operation
after

the entry has been added or marked
active

(refer to PMDA_CACHE_SAVE and PMDA_CACHE_SYNC below).
On success
pmdaCachePurge

returns the number of culled entries, else in the case of an error
the return value is negative (and suitable for decoding with
pmErrStr(3)).
pmdaCacheOp

may be used to perform additional operations on the cache as follows:

PMDA_CACHE_LOAD
The cache can optionally be maintained as a persistent external file,
so that the mapping of instance names to instance identifiers is persistent
across executions of a PMDA.
This operation loads the cache from the external file, and then
all new cache entries are marked
inactive,

and the additional
data pointer is set to NULL.
Entries loaded from the external file are checked against the current
cache contents and if the instance name and instance identifiers match
then the state in the cache (active

or
inactive)

is not changed. Should a mismatch be found (same instance name and
different instance identifier, or same instance identifier and different
instance name, or some but not all of the instance identifier,
the instance name and the ``hint'' match)
then the entry from the external file is ignored
and a warning is issued on
stderr.

Typically a PMDA would only
perform this operation once per execution.
PMDA_CACHE_SAVE
If any instance has been added to, or deleted from, the instance
domain since the last PMDA_CACHE_LOAD, PMDA_CACHE_SAVE or PMDA_CACHE_SYNC
operation, the
entire

cache is written to the external file as a bulk operation.
This operation is provided for PMDAs that are
not

interested
in using
pmdaCachePurge

and simply want the external file to reflect the set of known instances
without accurate details of when they were last marked
active.
Returns the number of instances saved to the external file, else 0
if the external file was already up to date.


PMDA_CACHE_STRINGS
Annotates this cache as being a special-purpose cache used for string
de-duplication in PMDAs exporting large numbers of string valued metrics.
This can be used to reduce the memory footprint of the PMDA (duplicate
strings hash to the same bucket, and are stored in memory once only).
Key comparisons are not terminated at the first space but rather the
entire string is used for matching.
These are specialised caches not useful for general purpose instance
domain handling.
PMDA_CACHE_SYNC
Within an instance domain,
if any instance has been added to, or deleted from, or marked
active

since the last PMDA_CACHE_LOAD, PMDA_CACHE_SAVE or PMDA_CACHE_SYNC
operation, the
entire

cache is written to the external file as a bulk operation.
This operation is similar to PMDA_CACHE_SAVE, but will save the
instance domain more frequently so the timestamps more
accurately match the semantics expected by
pmdaCachePurge.
Returns the number of instances saved to the external file, else 0
if the external file was already synchronized.


PMDA_CACHE_CHECK
Returns 1 if a cache exists for the specified instance domain,
else 0.
PMDA_CACHE_REUSE
When a new instance is added to the cache,
the default strategy is to assign instance identifiers in a monotonic
increasing
manner.  Once the maximum possible instance identifier value has been
assigned, the strategy changes to one where starting from 0,
the next available unused instance identifier will be used.
Calling
pmdaCacheOp

with PMDA_CACHE_REUSE forces an irreversible change to a second
(reuse) strategy where the next unallocated instance identifier
will be used.  This may be useful in cases where there is a
desire to restrict the allocated instance identifiers to smaller
values.  The prevailing strategy will be saved and restored across
PMDA_CACHE_SAVE and PMDA_CACHE_LOAD operations.
If
pmdaCacheStoreKey

is ever used, the associated instance domain will be changed to
PMDA_CACHE_REUSE mode.
PMDA_CACHE_REORG
Reorganize the cache to allow faster retrieval of
active

entries, and the cost of slower retrieval for
inactive

entries, and reclaim any culled entries.  The cache may be internally
re-organized as entries are added, so this operation is not required
for most PMDAs.
PMDA_CACHE_WALK_REWIND
Prepares for a traversal of the cache in ascending instance identifier
sequence.
PMDA_CACHE_WALK_NEXT
Fetch the next
active

instance identifier from the cache.  Requires a prior
call using PMDA_CACHE_WALK_REWIND and will return -1 when all instances
have been processed.
Only one cache walk can be active at any given time, nesting calls
to PMDA_CACHE_WALK and PMDA_CACHE_REWIND will interfere with each
other.


PMDA_CACHE_ACTIVE
Changes
every

inactive

entry in the cache to be marked
active.

PMDA_CACHE_INACTIVE
Changes
every

active

entry in the cache to be marked
inactive.

PMDA_CACHE_CULL
Remove
every

entry from the cache.
PMDA_CACHE_SIZE
Return the number of entries in the cache (includes
active,

inactive

and any culled entries that have not yet been reclaimed).
PMDA_CACHE_SIZE_ACTIVE
Return the number of
active

entries in the cache.
PMDA_CACHE_SIZE_INACTIVE
Return the number of
inactive

entries in the cache.
PMDA_CACHE_DUMP
Dump the current state of the cache on
stderr.

PMDA_CACHE_DUMP_ALL
Like PMDA_CACHE_DUMP, but also dump the internal hashing structures
used to support lookup by instance name, lookup by instance identifier and
the collision statistics for ``hint'' hashing from
pmdaCacheStoreKey.
pmdaCacheOp

returns a non-negative value on success, and failure is indicated
by a negative return value (suitable for decoding
with
pmErrStr(3)).</code></pre>
<h2>Other Considerations</h2>
<p>When the <code>pmdaCache</code> routines are used for particular instance domain, <code>pmdaInstance (3)</code> and the instance domain enumeration behind <code><a href="/docs/linux/man/3-pmdafetch/">pmdaFetch</a></code>(3) will attempt to extract instance domain information from the cache, thereby avoiding reference to the <code>pmdaIndom</code> data structures that have historically been used to define instance domains and service instance requests. A PMDA can adopt a hybrid approach and choose to implement some instance domains via the traditional <code>pmdaIndom</code> method, and others via the <code>pmdaCache</code> approach, however attempts to manage the <i>same</i> instance domain by both methods will result in the <code>pmdaCache</code> method silently prevailing. </p>
<p> If <code>all</code> instances in a PMDA are to be serviced from a <code>pmdaCache</code> then a <code>pmdaIndom</code> is not required, and the <code>pmdaInit (3)</code> call becomes <code> </p>
<p> </code></p>
<pre> pmdaInit(dp, NULL, 0, metrictab, nmetrics);</pre>
<p>However, the PMDA will need to explicitly initialize the <code>indom</code> field of the <code>pmDesc</code> in the <i>metrictab</i> entries, as this cannot be done by <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3) if <i>indomtab</i> is missing entries for the instance domains maintained in the cache. </p>
<p> Independent of how the instance domain is being maintained, to refresh an instance domain prior to a fetch or an instance domain operation, the standard methods of a &#8220;wrapper&#8221; to the <code>pmdaInstance (3)</code> and <code>pmdaFetch (3)</code> methods should be used. </p>
<p> Refer to the <code>simple</code> PMDA source code for an example use of the <code>pmdaCache</code> routines. </p>
<p> When using <code>pmdaCacheStoreKey</code>, if there is a desire to ensure the given &#8220;hint&#8221; generates the same initial instance identifier across all platforms, then the caller should ensure the endian and word-size issues are considered, e.g. if the natural data structure used for the <i>key</i> is an array of 32-bit integers, then <code><a href="/docs/linux/man/3-htonl/">htonl</a></code>(3) should be used on each element of the array before calling <code>pmdaCacheStoreKey</code> or <code>pmdaCacheLookupKey</code>.</p>
<h2>Instance Name Matching</h2>
<p>The following table summarizes the &#8220;short name&#8221; matching semantics for an instance domain (caches other than PMDA_CACHE_STRINGS style). <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>name in</td>
<td><code>pmdaCacheLookup</code></td>
<td VALIGN=center ROWSPAN=2>result
</td>
</tr>
<tr VALIGN=top>
<td>cache</td>
<td>name</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>foodle</td>
<td>foo</td>
<td>no match (PM_ERR_INST)
</td>
</tr>
<tr VALIGN=top>
<td>foo</td>
<td>foodle</td>
<td>no match (PM_ERR_INST)
</td>
</tr>
<tr VALIGN=top>
<td>foo</td>
<td>foo</td>
<td>match
</td>
</tr>
<tr VALIGN=top>
<td>foo bar</td>
<td>foo</td>
<td>match on short name (instance identifier)
</td>
</tr>
<tr VALIGN=top>
<td>foo bar</td>
<td>foo bar</td>
<td>match on full name (instance identifier)
</td>
</tr>
<tr VALIGN=top>
<td>foo</td>
<td>foo bar</td>
<td>bad match (-EDOM)
</td>
</tr>
<tr VALIGN=top>
<td>foo bar</td>
<td>foo blah</td>
<td>bad match (-EDOM)
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>Files</h2>
<p>Cache persistence uses files with names constructed from the <i>indom</i> within the <code>$PCP_VAR_DIR/config/pmda</code> directory.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-byteorder/">BYTEORDER</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3), <code><a href="/docs/linux/man/3-pmdainstance/">pmdaInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmdafetch/">pmdaFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmdasetfetchcallback/">pmdaSetFetchCallback</a></code>(3), <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3) and <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3). </p>
