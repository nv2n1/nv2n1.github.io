---
title: "auparse_normalize_functions(3)"
name: "auparse_normalize_functions"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_normalize_functions/"
description: "auparse_normalize_get_event_kind, auparse_normalize_get_action, auparse_normalize_object_kind, auparse_normalize_how, auparse_normalize_session, auparse_normalize_subject_primary, auparse_normalize..."
---

<h2>NAME</h2>
<pre>
auparse_normalize_get_event_kind, auparse_normalize_get_action, auparse_normalize_object_kind, auparse_normalize_how, auparse_normalize_session, auparse_normalize_subject_primary, auparse_normalize_subject_secondary, auparse_normalize_subject_first_attribute, auparse_normalize_subject_next_attribute, auparse_normalize_object_primary, auparse_normalize_object_secondary, auparse_normalize_object_first_attribute, auparse_normalize_object_next_attribute, auparse_normalize_get_results, auparse_normalize_key - Access normalized fields
</pre>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;auparse.h&gt;
Metadata Functions : const char *auparse_normalize_get_event_kind(auparse_state_t *au);
const char *auparse_normalize_get_action(auparse_state_t *au);
const char *auparse_normalize_object_kind(auparse_state_t *au);
const char *auparse_normalize_how(auparse_state_t *au);
Positioning Functions : int auparse_normalize_session(auparse_state_t *au);
int auparse_normalize_subject_primary(auparse_state_t *au);
int auparse_normalize_subject_secondary(auparse_state_t *au);
int auparse_normalize_subject_first_attribute(auparse_state_t *au);
int auparse_normalize_subject_next_attribute(auparse_state_t *au);
int auparse_normalize_object_primary(auparse_state_t *au);
int auparse_normalize_object_secondary(auparse_state_t *au);
int auparse_normalize_object_first_attribute(auparse_state_t *au);
int auparse_normalize_object_next_attribute(auparse_state_t *au);
int auparse_normalize_get_results(auparse_state_t *au);
int auparse_normalize_key(auparse_state_t *au);
</code></pre>
<h2>DESCRIPTION</h2>
<p> After calling the <code>auparse_normalize</code> function, you will probably want to access the audit event data. These function provide access to the results of the normalization. There are 2 kinds of function, metadata and positioning. </p>
<p> The metadata functions all return a pointer to a string that describes something about the event. This data does not live inside the event but is kept in lookup tables inside the auparse library. </p>
<p> The positioning function are different in that they move the internal cursor of auparse to the record and field that contains the information you want. You then use field accessor functions to retrieve the values. </p>
<h2>RETURN VALUE</h2>
<p> The positioning functions return &lt; 0 on error, 0 if uninitialized, and 1 on success. The metadata functions return NULL on error and a pointer to a string on success. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-auparse_normalize/">auparse_normalize</a>(3), <a href="/docs/linux/man/3-auparse_get_field_str/">auparse_get_field_str</a>(3), <a href="/docs/linux/man/3-auparse_interpret_field/">auparse_interpret_field</a>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
