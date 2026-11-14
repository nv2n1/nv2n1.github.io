---
title: "drmaa2_dict(3)"
name: "drmaa2_dict"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa2_dict/"
description: "drmaa2_dict_create, drmaa2_dict_free, drmaa2_dict_list, drmaa2_dict_has, drmaa2_dict_get, drmaa2_dict_del, drmaa2_dict_set – DRMAA2 dictionary routines"
---

<h2 class="name">NAME</h2>
<p> drmaa2_dict_create, drmaa2_dict_free, drmaa2_dict_list, drmaa2_dict_has, drmaa2_dict_get, drmaa2_dict_del, drmaa2_dict_set &#8211; DRMAA2 dictionary routines </p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre><code>
typedef struct drmaa2_dict_s *drmaa2_dict;
typedef void (*drmaa2_dict_entryfree)(char **key, char **val);
drmaa2_dict drmaa2_dict_create(const drmaa2_dict_entryfree callback);
void drmaa2_dict_free(drmaa2_dict *d);
drmaa2_string_list drmaa2_dict_list(const drmaa2_dict d);
drmaa2_bool drmaa2_dict_has(const drmaa2_dict d, const char *key);
const char *drmaa2_dict_get(const drmaa2_dict d, const char *key);
drmaa2_error drmaa2_dict_del(drmaa2_dict d, const char *key);
drmaa2_error drmaa2_dict_set(drmaa2_dict d, const char *key, const char *val);
</code></pre>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>drmaa2_dict_create</code>()</p>
<dd> creates a new dictionary instance. Returns a pointer to the dictionary or NULL on error. Optional parameter <i>callback</i> allows the application to provide a callback pointer to a collection element cleanup function. <code>DRMAA2_UNSET_CALLBACK</code> may be supplied instead of a valid callback pointer.</p>
<dt><code>drmaa2_dict_free</code>()</p>
<dd> frees the dictionary and the contained members. If a callback function was provided on dictionary creation, it SHALL be called once per dictionary entry.</p>
<dt><code>drmaa2_dict_list</code>()</p>
<dd> gets all dictionary keys as DRMAA <code>drmaa2_string_list</code>. If the dictionary is empty, a valid string list with zero elements SHALL be returned. The application is expected to use <code>drmaa2_list_free</code> for freeing the returned data structure.</p>
<dt><code>drmaa2_dict_has</code>()</p>
<dd> returns a boolean indication if the given key exists in the dictionary. On error, the function SHALL return FALSE.</p>
<dt><code>drmaa2_dict_get</code>()</p>
<dd> gets the dictionary value for the specified key. If the key is invalid, the function returns NULL.</p>
<dt><code>drmaa2_dict_del</code>()</p>
<dd> removes the dictionary entry with the given key and returns a success indication. If a callback function was provided on dictionary creation, it SHALL be called before this function returns.</p>
<dt><code>drmaa2_dict_set</code>()</p>
<dd> sets the specified dictionary key to the specified value. Key and value strings MUST be stored as the provided character pointers. If the dictionary already has an entry for this name, the value is replaced and the old value is removed. If a callback was provided on dictionary creation, it SHALL be called with a NULL pointer for the key and the pointer of the previous value.</dl>
<h2>SEE ALSO</h2>
<h2>Index</h2>
