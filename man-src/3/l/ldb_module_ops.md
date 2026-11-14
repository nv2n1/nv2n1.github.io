---
title: "ldb_module_ops(3)"
name: "ldb_module_ops"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_module_ops/"
description: "ldb_module_ops –"
---

<h2 class="name">NAME</h2>
<p> ldb_module_ops &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> const char * <code>name</code> </p>
<p> int(* <code>init_context</code> )(struct <code>ldb_module</code> *) </p>
<p> int(* <code>search</code> )(struct <code>ldb_module</code> *, struct <code>ldb_request</code> *) </p>
<p> int(* <code>add</code> )(struct <code>ldb_module</code> *, struct <code>ldb_request</code> *) </p>
<p> int(* <code>modify</code> )(struct <code>ldb_module</code> *, struct <code>ldb_request</code> *) </p>
<p> int(* <code>del</code> )(struct <code>ldb_module</code> *, struct <code>ldb_request</code> *) </p>
<p> int(* <code>rename</code> )(struct <code>ldb_module</code> *, struct <code>ldb_request</code> *) </p>
<p> int(* <code>request</code> )(struct <code>ldb_module</code> *, struct <code>ldb_request</code> *) </p>
<p> int(* <code>extended</code> )(struct <code>ldb_module</code> *, struct <code>ldb_request</code> *) </p>
<p> int(* <code>start_transaction</code> )(struct <code>ldb_module</code> *) </p>
<p> int(* <code>prepare_commit</code> )(struct <code>ldb_module</code> *) </p>
<p> int(* <code>end_transaction</code> )(struct <code>ldb_module</code> *) </p>
<p> int(* <code>del_transaction</code> )(struct <code>ldb_module</code> *) </p>
<p> int(* <code>sequence_number</code> )(struct <code>ldb_module</code> *, struct <code>ldb_request</code> *) </p>
<p> void * <code>private_data</code> </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code. </p>
<h2>Index</h2>
