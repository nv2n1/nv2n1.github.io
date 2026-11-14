---
title: "stdexperimentalnonesuch(3)"
name: "stdexperimentalnonesuch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalnonesuch/"
---

std::experimental::nonesuch - std::experimental::nonesuch

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / type_traits&gt;

    struct nonesuch {

    ~nonesuch() = delete;

    nonesuch(nonesuch const &amp;) = delete;
    (library fundamentals TS v2)

        void
        operator=(nonesuch const &amp;) = delete;
};</code></pre> 
std::experimental::nonesuch is a class type used by std::experimental::detected_t to indicate detection failure. 
nonesuch has no default constructor or initializer-list constructor, and is not an aggregate. 

<h2>Notes</h2>

nonesuch cannot be constructed, destroyed, or copied. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2960 LFTSv2 nonesuch may be an aggregate and has an implicit conversion sequence from {} made non-aggregate and removed ICS 
