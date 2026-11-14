---
title: "snap-discard-ns(8)"
name: "snap-discard-ns"
section: "8"
letter: "s"
url: "/docs/linux/man/8-snap-discard-ns/"
---

snap-discard-ns - internal tool for discarding preserved namespaces of snappy applications

<h2>Synopsis</h2>

snap-discard-ns [--from-snap-confine] SNAP_INSTANCE_NAME

<h2>Description</h2>

The <i>snap-discard-ns</i> is a program used internally by <i>snapd</i> to discard a preserved mount namespace of a particular snap.

<h2>Options</h2>

The --from-snap-confine option is used internally by snap-confine to tell snap-discard-ns that it is invoked from snap-confine and can disable locking.

<h2>Environment</h2>

<i>snap-discard-ns</i> responds to the following environment variables
<dl><dt><i>SNAP_CONFINE_DEBUG</i>:
<dd>When defined the program will print additional diagnostic information about the actions being performed. All the output goes to stderr.</dl>

<h2>Files</h2>

<i>snap-discard-ns</i> uses the following files: 

 <i>/run/snapd/ns/$SNAP_INSTNACE_NAME.mnt</i>: <i>/run/snapd/ns/$SNAP_INSTNACE_NAME.*.mnt</i>: The preserved mount namespace that is unmounted and removed by <i>snap-discard-ns</i>. The second form is for the per-user mount namespace. 

 <i>/run/snapd/ns/snap.$SNAP_INSTNACE_NAME.fstab</i>: <i>/run/snapd/ns/snap.$SNAP_INSTNACE_NAME.*.user-fstab</i>: The current mount profile of a preserved mount namespace that is removed by <i>snap-discard-ns</i>.

<h2>Bugs</h2>

Please report all bugs with <i><a rel="nofollow" HREF="https://bugs.launchpad.net/snapd/+filebug">https://bugs.launchpad.net/snapd/+filebug</a></i>

<h2>Author</h2>

zygmunt.krynicki [at] canonical.com

<h2>Copyright</h2>

Canonical Ltd.
