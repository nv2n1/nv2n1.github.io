---
title: "efadv(7)"
name: "efadv"
section: "7"
letter: "e"
url: "/docs/linux/man/7-efadv/"
---

efadv - Direct verbs for efa devices 

 This provides low level access to efa devices to perform direct operations, without general branching performed by libibverbs.

<h2>Description</h2>

The libibverbs API is an abstract one. It is agnostic to any underlying provider specific implementation. While this abstraction has the advantage of user applications portability, it has a performance penalty. For some applications optimizing performance is more important than portability. 

 The efa direct verbs API is intended for such applications. It exposes efa specific low level operations, allowing the application to bypass the libibverbs API. 

 The direct include of efadv.h together with linkage to efa library will allow usage of this new interface.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-verbs/">verbs</a>(7)

<h2>Authors</h2>

Gal Pressman &lt;galpress [at] amazon.com&gt;
