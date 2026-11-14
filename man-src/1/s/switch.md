---
title: "switch(1)"
name: "switch"
section: "1"
letter: "s"
url: "/docs/linux/man/1-switch/"
---

<h2 class="name">NAME</h2>
 

 switch - conditionally execute a block of commands

<h3>Synopsis</h3>

 switch VALUE; [case [WILDCARD...]; [COMMANDS...]; ...] end

<h3>Description</h3>

 The switch statement is used to perform one of several blocks of commands depending on whether a specified value equals one of several wildcarded values. The case statement is used together with the switch statement in order to determine which block should be performed. 

 Each case command is given one or more parameter. The first case command with a parameter that matches the string specified in the switch command will be evaluated. case parameters may contain wildcards. These need to be escaped or quoted in order to avoid regular wildcard expansion using filenames. 

 Note that fish does not fall through on case statements. Though the syntax may look a bit like C switch statements, it behaves more like the case statements of traditional shells. 

 Also note that command substitutions in a case statement will be evaluated even if it's body is not taken. This may seem counterintuitive at first, but it is unavoidable, since it would be impossible to know if a case command will evaluate to true before all forms of parameter expansion have been performed for the case command.

<h3>Example</h3>

 If the variable $animal contains the name of an animal, the following code would attempt to classify it: 

 

 <pre><code>
switch
$animal case cat
    echo evil case wolf dog human moose dolphin whale
        echo mammal case duck goose albatross
            echo bird case shark trout stingray
                echo fish case '*' echo I have no idea what a $animal is
                    end
</code></pre> 

 

 If the above code was run with $animal set to whale, the output would be mammal. 

<h2>Index</h2>


