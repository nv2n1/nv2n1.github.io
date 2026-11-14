---
title: "stdalign_val_t(3)"
name: "stdalign_val_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdalign_val_t/"
---

std::align_val_t - std::align_val_t

<h2>Synopsis</h2>

Defined in header &lt;new&gt; 
enum class align_val_t : std::size_t {}; <i>(since C++17)</i> 
Both new-expression and delete-expression, when used with objects whose alignment requirement is greater than __STDCPP_DEFAULT_NEW_ALIGNMENT__, pass that alignment requirement as an argument of type std::align_val_t to the selected allocation/deallocation function. 

<h2>Notes</h2>

Alignment (as obtained by alignof) has the type std::size_t, but placement forms of allocation and deallocation functions that take std::size_t as an additional parameter are already in use, so this type is used instead. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions 
operator_new <i>(function)</i> 
operator_new[] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocation functions 
operator_delete <i>(function)</i> 
operator_delete[] 
