---
title: "stdis_constant_evaluated(3)"
name: "stdis_constant_evaluated"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_constant_evaluated/"
---

std::is_constant_evaluated - std::is_constant_evaluated

<h2>Synopsis</h2>

Defined in header &lt;type_traits&gt; 
constexpr bool is_constant_evaluated() noexcept; <i>(since C++20)</i> 
Detects whether the function call occurs within a constant-evaluated context. Returns true if the evaluation of the call occurs within the evaluation of an expression or conversion that is manifestly constant-evaluated; otherwise returns false. 
The following expressions (including conversions to the destination type) are manifestly constant-evaluated: 
* Where a constant expression is grammatically required, including: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* array_bounds 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* the dimensions in new-expressions other than the first 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* bit-field_lengths 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* enumeration_initializers 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* alignments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* case_expressions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* non-type template_arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* expressions in noexcept_specifications 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* expressions in static_assert_declarations 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* expressions in conditional_explicit_specifiers 
* conditions of constexpr_if_statements 
* immediate_invocations 
* constraint expressions in concept definitions, nested_requirements, and requires_clauses 
* initializers of variables that are usable in constant expressions, including: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* initializers of constexpr_variables 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* initializers of variables with reference type or const-qualified integral or enumeration type, when the initializers are constant_expressions 
* initializers of static and thread local variables, when all subexpressions of the initializers (including constructor calls and implicit conversions) are constant_expressions (that is, when the initializers are constant_initializers) 
To test the last two conditions, compilers may first perform a trial constant evaluation of the initializers. It is not recommended to depend on the result in this case. <pre><code>int y;

const int a = std::is_constant_evaluated() ? y : 1;

// Trial constant evaluation fails. The constant evaluation is discarded.

// Variable a is dynamically initialized with 1
const int b = std::is_constant_evaluated() ? 2 : y;

// Constant evaluation with std::is_constant_evaluation() == true succeeds.

// Variable b is statically initialized with 2
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the evaluation of the call occurs within the evaluation of an expression or conversion that is manifestly constant-evaluated; otherwise false 

<h2>Notes</h2>

When directly used as the condition of static_assert_declaration or constexpr_if_statement, std::is_constant_evaluated() always returns true. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
