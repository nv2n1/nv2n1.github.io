---
title: "units(1)"
name: "units"
section: "1"
letter: "u"
url: "/docs/linux/man/1-units/"
description: "units — unit conversion and calculation program"
---

<h2 class="name">NAME</h2>
<p> units &#8212; unit conversion and calculation program</p>
<h2>SYNOPSIS</h2>
<p> &#8216;units&#8217; [<i>options</i>] [<i>from-unit</i> [<i>to-unit</i>]] </p>
<h2>DESCRIPTION</h2>
<p> The &#8216;units&#8217; program converts quantities expressed in various systems of measurement to their equivalents in other systems of measurement. Like many similar programs, it can handle multiplicative scale changes. It can also handle nonlinear conversions such as Fahrenheit to Celsius. See the examples below. The program can also perform conversions from and to sums of units, such as converting between meters and feet plus inches. </p>
<p> Beyond simple unit conversions, &#8216;units&#8217; can be used as a general-purpose scientific calculator that keeps track of units in its calculations. You can form arbitrary complex mathematical expressions of dimensions including sums, products, quotients, powers, and even roots of dimensions. Thus you can ensure accuracy and dimensional consistency when working with long expressions that involve many different units that may combine in complex ways. </p>
<p> The units are defined in an external data file. You can use the extensive data file that comes with this program, or you can provide your own data file to suit your needs. You can also use your own data file to supplement the standard data file. </p>
<p> Basic operation is simple: you enter the units that you want to convert <i>from</i> and the units that you want to convert <i>to</i>. You can use the program interactively with prompts, or you can use it from the command line. </p>
<h2>INTERACTING WITH UNITS</h2>
<p> To invoke units for interactive use, type &#8216;<i>units</i>&#8216; at your shell prompt. The program will print something like this: </p>
<pre>
Currency exchange rates from 04/23/12 
2516 units, 85 prefixes, 65 nonlinear units
    
You have:
</pre>
<p> At the &#8216;You have:&#8217; prompt, type the quantity and units that you are converting <i>from</i>. For example, if you want to convert ten meters to feet, type &#8216;<i>10 meters</i>&#8216;. Next, &#8216;units&#8217; will print &#8216;You want:&#8217;. You should type the units you want to convert <i>to</i>. To convert to feet, you would type &#8216;<i>feet</i>&#8216;. If the &#8216;readline&#8217; library was compiled in then the tab key can be used to complete unit names. See <i>Readline Support</i> for more information about &#8216;readline&#8217;. To quit the program press Ctrl-C or Ctrl-D under Unix. Under Windows press Ctrl-Z. </p>
<p> The answer will be displayed in two ways. The first line of output, which is marked with a &#8216;*&#8217; to indicate multiplication, gives the result of the conversion you have asked for. The second line of output, which is marked with a &#8216;/&#8217; to indicate division, gives the inverse of the conversion factor. If you convert 10 meters to feet, &#8216;units&#8217; will print </p>
<pre>
    * 32.808399
    / 0.03048
</pre>
<p> which tells you that 10 meters equals about 32.8 feet. The second number gives the conversion in the opposite direction. In this case, it tells you that 1 foot is equal to about 0.03 dekameters since the dekameter is 10 meters. It also tells you that 1/32.8 is about 0.03. </p>
<p> The &#8216;units&#8217; program prints the inverse because sometimes it is a more convenient number. In the example above, for example, the inverse value is an exact conversion: a foot is exactly 0.03048 dekameters. But the number given the other direction is inexact. </p>
<p> If you convert grains to pounds, you will see the following: </p>
<pre>
You have: grains
You want: pounds
        * 0.00014285714
        / 7000
</pre>
<p>From the second line of the output you can immediately see that a grain is equal to a seven thousandth of a pound. This is not so obvious from the first line of the output. If you find the output format confusing, try using the &#8216;&#8211;verbose&#8217; option: </p>
<pre>
You have: grain
You want: aeginamina
        grain = 0.00010416667 aeginamina
        grain = (1 / 9600) aeginamina
</pre>
<p> If you request a conversion between units that measure reciprocal dimensions, then &#8216;units&#8217; will display the conversion results with an extra note indicating that reciprocal conversion has been done: </p>
<pre>
You have: 6 ohms
You want: siemens
        reciprocal conversion
        * 0.16666667
        / 6
</pre>
<p> Reciprocal conversion can be suppressed by using the &#8216;&#8211;strict&#8217; option. As usual, use the &#8216;&#8211;verbose&#8217; option to get more comprehensible output: </p>
<pre>
You have: tex
You want: typp
        reciprocal conversion
        1 / tex = 496.05465 typp
        1 / tex = (1 / 0.0020159069) typp
You have: 20 mph
You want: sec/mile
        reciprocal conversion
        1 / 20 mph = 180 sec/mile
        1 / 20 mph = (1 / 0.0055555556) sec/mile
</pre>
<p> If you enter incompatible unit types, the &#8216;units&#8217; program will print a message indicating that the units are not conformable and it will display the reduced form for each unit: </p>
<pre>
You have: ergs/hour
You want: fathoms kg^2 / day 
conformability error
        2.7777778e-11 kg m^2 / sec^3
        2.1166667e-05 kg^2 m / sec
</pre>
<p> If you only want to find the reduced form or definition of a unit, simply press <i>Enter</i> at the &#8216;You want:&#8217; prompt. Here is an example: </p>
<pre>
You have: jansky
You want: 
        Definition: fluxunit = 1e-26 W/m^2 Hz = 1e-26 kg / s^2
</pre>
<p> The output from &#8216;units&#8217; indicates that the jansky is defined to be equal to a fluxunit which in turn is defined to be a certain combination of watts, meters, and hertz. The fully reduced (and in this case somewhat more cryptic) form appears on the far right. </p>
<p> Some named units are treated as dimensionless in some situations. These units include the radian and steradian. These units will be treated as equal to 1 in units conversions. Power is equal to torque times angular velocity. This conversion can only be performed if the radian is dimensionless. </p>
<pre>
You have: (14 ft lbf) (12 radians/sec)
You want: watts
        * 227.77742
        / 0.0043902509
</pre>
<p> Named dimensionless units are not treated as dimensionless in other contexts. They cannot be used as exponents so for example, &#8216;meter^radian&#8217; is not allowed. </p>
<p> If you want a list of options you can type &#8216;<i>?</i>&#8216; at the &#8216;You want:&#8217; prompt. The program will display a list of named units that are conformable with the unit that you entered at the &#8216;You have:&#8217; prompt above. Conformable unit <i>combinations</i> will not appear on this list. </p>
<p> Typing &#8216;<i>help</i>&#8216; at either prompt displays a short help message. You can also type &#8216;<i>help</i>&#8216; followed by a unit name. This will invoke a pager on the units data base at the point where that unit is defined. You can read the definition and comments that may give more details or historical information about the unit. (You can generally quit out of the page by pressing &#8216;q&#8217;.) </p>
<p> Typing &#8216;<i>search</i>&#8216; <i>text</i> will display a list of all of the units whose names contain <i>text</i> as a substring along with their definitions. This may help in the case where you aren&#8217;t sure of the right unit name. </p>
<h2>USING UNITS NON-INTERACTIVELY</h2>
<p> The &#8216;units&#8217; program can perform units conversions non-interactively from the command line. To do this, type the command, type the original unit expression, and type the new units you want. If a units expression contains non-alphanumeric characters, you may need to protect it from interpretation by the shell using single or double quote characters. </p>
<p> If you type </p>
<pre>
units &quot;2 liters&quot; quarts
</pre>
<p> then &#8216;units&#8217; will print </p>
<pre>
    * 2.1133764
    / 0.47317647
</pre>
<p> and then exit. The output tells you that 2 liters is about 2.1 quarts, or alternatively that a quart is about 0.47 times 2 liters. </p>
<p> If the conversion is successful, then &#8216;units&#8217; will return success (zero) to the calling environment. If you enter non-conformable units then &#8216;units&#8217; will print a message giving the reduced form of each unit and it will return failure (nonzero) to the calling environment. </p>
<p> When you invoke &#8216;units&#8217; with only one argument, it will print out the definition of the specified unit. It will return failure if the unit is not defined and success if the unit is defined. </p>
<h2>UNIT DEFINITIONS</h2>
<p> The conversion information is read from a units data file that is called &#8216;definitions.units&#8217; and is usually located in the &#8216;/usr/share/units&#8217; directory. If you invoke &#8216;units&#8217; with the &#8216;-V&#8217; option, it will print the location of this file. The default file includes definitions for all familiar units, abbreviations and metric prefixes. It also includes many obscure or archaic units. </p>
<p> Many constants of nature are defined, including these: </p>
<pre>
pi          ratio of circumference to diameter
c           speed of light
e           charge on an electron
force       acceleration of gravity
mole        Avogadro's number
water       pressure per unit height of water
Hg          pressure per unit height of mercury
au          astronomical unit
k           Boltzman's constant
mu0         permeability of vacuum
epsilon0    permittivity of vacuum
G           Gravitational constant
mach        speed of sound
</pre>
<p> The standard data file includes atomic masses for all of the elements and numerous other constants. Also included are the densities of various ingredients used in baking so that &#8216;2 cups flour_sifted&#8217; can be converted to &#8216;grams&#8217;. This is not an exhaustive list. Consult the units data file to see the complete list, or to see the definitions that are used. </p>
<p> The &#8216;pound&#8217; is a unit of mass. To get force, multiply by the force conversion unit &#8216;force&#8217; or use the shorthand &#8216;lbf&#8217;. (Note that &#8216;g&#8217; is already taken as the standard abbreviation for the gram.) The unit &#8216;ounce&#8217; is also a unit of mass. The fluid ounce is &#8216;fluidounce&#8217; or &#8216;floz&#8217;. British capacity units that differ from their US counterparts, such as the British Imperial gallon, are prefixed with &#8216;br&#8217;. Currency is prefixed with its country name: &#8216;belgiumfranc&#8217;, &#8216;britainpound&#8217;. </p>
<p> When searching for a unit, if the specified string does not appear exactly as a unit name, then the &#8216;units&#8217; program will try to remove a trailing &#8216;s&#8217;, &#8216;es&#8217;. Next units will replace a trailing &#8216;ies&#8217; with &#8216;y&#8217;. If that fails, &#8216;units&#8217; will check for a prefix. The database includes all of the standard metric prefixes. Only one prefix is permitted per unit, so &#8216;micromicrofarad&#8217; will fail. However, prefixes can appear alone with no unit following them, so &#8216;micro*microfarad&#8217; will work, as will &#8216;micro microfarad&#8217;. </p>
<p> To find out which units and prefixes are available, read the standard units data file, which is extensively annotated. </p>
<h3>English Customary Units</h3>
<p> English customary units differ in various ways in different regions. In Britain a complex system of volume measurements featured different gallons for different materials such as a wine gallon and ale gallon that different by twenty percent. This complexity was swept away in 1824 by a reform that created an entirely new gallon, the British Imperial gallon defined as the volume occupied by ten pounds of water. Meanwhile in the USA the gallon is derived from the 1707 Winchester wine gallon, which is 231 cubic inches. These gallons differ by about twenty percent. By default if &#8216;units&#8217; runs in the &#8216;en_GB&#8217; locale you will get the British volume measures. If it runs in the &#8216;en_US&#8217; locale you will get the US volume measures. In other locales the default values are the US definitions. If you wish to force different definitions then set the environment variable &#8216;UNITS_ENGLISH&#8217; to either &#8216;US&#8217; or &#8216;GB&#8217; to set the desired definitions independent of the locale. </p>
<p> Before 1959, the value of a yard (and other units of measure defined in terms of it) differed slightly among English-speaking countries. In 1959, Australia, Canada, New Zealand, the United Kingdom, the United States, and South Africa adopted the Canadian value of 1 yard = 0.9144 m (exactly), which was approximately halfway between the values used by the UK and the US; it had the additional advantage of making 1 inch = 2.54 cm (exactly). This new standard was termed the <i>International Yard</i>. Australia, Canada, and the UK then defined all customary lengths in terms of the International Yard (Australia did not define the furlong or rod); because many US land surveys were in terms of the pre-1959 units, the US continued to define customary surveyors&#8217; units (furlong, chain, rod, and link) in terms of the previous value for the foot, which was termed the <i>US survey foot</i>. The US defined a <i>US survey mile</i> as 5280 US survey feet, and defined a <i>statute mile</i> as a US survey mile. The US values for these units differ from the international values by about 2 ppm. </p>
<p> The &#8216;units&#8217; program uses the international values for these units; the US values can be obtained by using either the &#8216;US&#8217; or the &#8216;survey&#8217; prefix. In either case, the simple familiar relationships among the units are maintained, e.g., 1 &#8216;furlong&#8217; = 660 &#8216;ft&#8217;, and 1 &#8216;USfurlong&#8217; = 660 &#8216;USft&#8217;, though the metric equivalents differ slightly between the two cases. The &#8216;US&#8217; prefix or the &#8216;survey&#8217; prefix can also be used to obtain the US survey mile and the value of the US yard prior to 1959, e.g., &#8216;USmile&#8217; or &#8216;surveymile&#8217; (but <i>not</i> &#8216;USsurveymile&#8217;). To get the US value of the statute mile, use either &#8216;USstatutemile&#8217; or &#8216;USmile&#8217;. </p>
<p> Except for distances that extend over hundreds of miles (such as in the US State Plane Coordinate System), the differences in the miles are usually insignificant: </p>
<pre>
You have: 100 surveymile - 100 mile
You want: inch
        * 12.672025
        / 0.078913984
</pre>
<p> The pre-1959 UK values for these units can be obtained with the prefix &#8216;UK&#8217;. </p>
<p> In the US, the acre is officially defined in terms of the US survey foot, but &#8216;units&#8217; uses a definition based on the international foot. If you want the official US acre use &#8216;USacre&#8217; and similarly use &#8216;USacrefoot&#8217; for the official US version of that unit. The difference between these units is about 4 parts per million. </p>
<h2>UNIT EXPRESSIONS</h2>
<h3>Operators</h3>
<p> You can enter more complicated units by combining units with operations such as powers, multiplication, division, addition, subtraction, and parentheses for grouping. You can use the customary symbols for these operators when &#8216;units&#8217; is invoked with its default options. Additionally, &#8216;units&#8217; supports some extensions, including high priority multiplication using a space, and a high priority numerical<br />
&nbsp;<wbr>division operator &#8216;(&#8216;| that can simplify some expressions. </p>
<p> Powers of units can be specified using the &#8216;^&#8217; character as shown in the following example, or by simple concatenation of a unit and its exponent: &#8216;cm3&#8217; is equivalent to &#8216;cm^3&#8217;; if the exponent is more than one digit, the &#8216;^&#8217; is required. An exponent like &#8216;2^3^2&#8217; is evaluated right to left as usual. The &#8216;^&#8217; operator has the second highest precedence. You can also use &#8216;**&#8217; as an exponent operator. </p>
<pre>
You have: cm^3
You want: gallons
        * 0.00026417205
        / 3785.4118
You have: arabicfoot * arabictradepound * force
You want: ft lbf  
        * 0.7296
        / 1.370614
</pre>
<p> You multiply units using a space or an asterisk &#8216;(&#8216;* The example above shows both forms. You can divide units using the slash &#8216;(&#8216;/ or with &#8216;per&#8217;. </p>
<pre>
You have: furlongs per fortnight
You want: m/s  
        * 0.00016630986
        / 6012.8727
</pre>
<p> When a unit includes a prefix, exponent operators apply to the combination, so &#8216;centimeter^3&#8217; gives cubic centimeters. If you separate the prefix from the unit with any multiplication operator, such as &#8216;centi meter^3&#8217;, then the prefix is treated as a separate unit, so the exponent does not apply. The second example would be a hundredth of a cubic meter, not a centimeter. </p>
<p> Multiplication using a space has a higher precedence than division using a slash and is evaluated left to right; in effect, the first &#8216;/&#8217; character marks the beginning of the denominator of a unit expression. This makes it simple to enter a quotient with several terms in the denominator: &#8216;W / m^2 Hz&#8217;. If you multiply with &#8216;*&#8217; then you must group the terms in the denominator with parentheses: &#8216;W / (m^2 * Hz)&#8217;. </p>
<p> The higher precedence of the space operator may not always be advantageous. For example, &#8216;m/s s/day&#8217; is equivalent to &#8216;m / s s day&#8217; and has dimensions of length per time cubed. Similarly, &#8216;1/2 meter&#8217; refers to a unit of reciprocal length equivalent to 0.5/meter, perhaps not what you would intend if you entered that expression. The &#8216;*&#8217; operator is convenient for multiplying a sequence of quotients. With the &#8216;*&#8217; operator, the example above becomes &#8216;m/s * s/day&#8217;, which is equivalent to &#8216;m/day&#8217;. Similarly, you could write &#8216;1/2 * meter&#8217; to get half a meter. Alternatively, parentheses can be used for grouping: you could write &#8216;(1/2) meter&#8217; to get half a meter. See <i>Complicated Unit Expressions</i> for an illustration of the various options. </p>
<p> The &#8216;units&#8217; program supports another option for numerical fractions. You can indicate division of <i>numbers</i> with the vertical bar &#8216;(&#8216;| so if you wanted half a meter you could write &#8216;1|2 meter&#8217;. This operator has the highest precedence, so you can write the square root of two thirds &#8216;2|3^1|2&#8217;. You cannot use the vertical bar to indicate division of non-numerical units (e.g., &#8216;m|s&#8217; results in an error message). </p>
<pre>
You have: 1|2 inch
You want: cm
        * 1.27
        / 0.78740157
</pre>
<p> You can use parentheses for grouping: </p>
<pre>
You have: (1/2) kg / (kg/meter)
You want: league
        * 0.00010356166
        / 9656.0833
</pre>
<h3>Sums and Differences of Units</h3>
<p> Outside of the SI, it is sometimes desirable to add values of different units. You may also wish to use &#8216;units&#8217; as a calculator that keeps track of units. Sums of conformable units are written with the &#8216;+&#8217; character, and differences with the &#8216;-&#8216; character. </p>
<pre>
You have: 2 hours + 23 minutes + 32 seconds
You want: seconds
        * 8612
        / 0.00011611705
    
You have: 12 ft + 3 in
You want: cm
        * 373.38
        / 0.0026782366
You have: 2 btu + 450 ft lbf
You want: btu
        * 2.5782804
        / 0.38785542
</pre>
<p> The expressions that are added or subtracted must reduce to identical expressions in primitive units, or an error message will be displayed: </p>
<pre>
You have: 12 printerspoint - 4 heredium
                                      ^
Illegal sum of non-conformable units
</pre>
<p> As usual, the precedence for &#8216;+&#8217; and &#8216;-&#8216; is lower than that of the other operators. A fractional quantity such as 2 1/2 cups can be given as &#8216;(2+1|2) cups&#8217;; the parentheses are necessary because multiplication has higher precedence than addition. If you omit the parentheses, &#8216;units&#8217; attempts to add &#8216;2&#8217; and &#8216;1|2 cups&#8217;, and you get an error message: </p>
<pre>
You have: 2+1|2 cups
                   ^
Illegal sum or difference of non-conformable units
</pre>
<p> The expression could also be correctly written as &#8216;(2+1/2) cups&#8217;. If you write &#8216;2 1|2 cups&#8217; the space is interpreted as <i>multiplication</i> so the result is the same as &#8216;1 cup&#8217;. </p>
<p> The &#8216;+&#8217; and &#8216;-&#8216; characters sometimes appears in exponents like &#8216;3.43e+8&#8217;. This leads to an ambiguity in an expression like &#8216;3e+2 yC&#8217;. The unit &#8216;e&#8217; is a small unit of charge, so this can be regarded as equivalent to &#8216;(3e+2) yC&#8217; or &#8216;(3 e)+(2 yC)&#8217;. This ambiguity is resolved by always interpreting &#8216;+&#8217; and &#8216;-&#8216; as part of an exponent if possible. </p>
<h3>Numbers as Units</h3>
<p> For &#8216;units&#8217;, numbers are just another kind of unit. They can appear as many times as you like and in any order in a unit expression. For example, to find the volume of a box that is 2 ft by 3 ft by 12 ft in steres, you could do the following: </p>
<pre>
You have: 2 ft 3 ft 12 ft
You want: stere
        * 2.038813
        / 0.49048148
    
You have: $ 5 / yard
You want: cents / inch
        * 13.888889
        / 0.072
</pre>
<p> And the second example shows how the dollar sign in the units conversion can precede the five. Be careful: &#8216;units&#8217; will interpret &#8216;$5&#8217; with no space as equivalent to &#8216;dollar^5&#8217;. </p>
<h3>Built-in Functions</h3>
<p> Several built-in functions are provided: &#8216;sin&#8217;, &#8216;cos&#8217;, &#8216;tan&#8217;, &#8216;ln&#8217;, &#8216;log&#8217;, &#8216;log2&#8217;, &#8216;exp&#8217;, &#8216;acos&#8217;, &#8216;atan&#8217; and &#8216;asin&#8217;. The &#8216;sin&#8217;, &#8216;cos&#8217;, and &#8216;tan&#8217; functions require either a dimensionless argument or an argument with dimensions of angle. </p>
<pre>
You have: sin(30 degrees)
You want: 
        Definition: 0.5
You have: sin(pi/2)
You want:  
        Definition: 1
You have: sin(3 kg)
                  ^
Unit not dimensionless
</pre>
<p> The other functions on the list require dimensionless arguments. The inverse trigonometric functions return arguments with dimensions of angle. </p>
<p> If you wish to take roots of units, you may use the &#8216;sqrt&#8217; or &#8216;cuberoot&#8217; functions. These functions require that the argument have the appropriate root. You can obtain higher roots by using fractional exponents: </p>
<pre>
You have: sqrt(acre)
You want: feet
        * 208.71074
        / 0.0047913202
    
You have: (400 W/m^2 / stefanboltzmann)^(1/4)
You have:
        Definition: 289.80882 K
    
You have: cuberoot(hectare)
                          ^
Unit not a root
</pre>
<h3>Complicated Unit Expressions</h3>
<p> The &#8216;units&#8217; program is especially helpful in ensuring accuracy and dimensional consistency when converting lengthy unit expressions. For example, one form of the Darcy-Weisbach fluid-flow equation is</p>
<dl>
<dt>
<dd>
<p> Delta <i>P</i> = (8 / pi)^2 (rho <i>fLQ</i>^2) / <i>d</i>^5,</dl>
<p> where Delta <i>P</i> is the pressure drop, rho is the mass density, <i>f</i> is the (dimensionless) friction factor, <i>L</i> is the length of the pipe, <i>Q</i> is the volumetric flow rate, and <i>d</i> is the pipe diameter. It might be desired to have the equation in the form</p>
<dl>
<dt>
<dd>
<p> Delta <i>P</i> = A1 rho <i>fLQ</i>^2 / <i>d</i>^5</dl>
<p> that accepted the user&#8217;s normal units; for typical units used in the US, the required conversion could be something like </p>
<pre>
You have: (8/pi^2)(lbm/ft^3)ft(ft^3/s)^2(1/in^5)
You want: psi
        * 43.533969
        / 0.022970568
</pre>
<p> The parentheses allow individual terms in the expression to be entered naturally, as they might be read from the formula. Alternatively, the multiplication could be done with the &#8216;*&#8217; rather than a space; then parentheses are needed only around &#8216;ft^3/s&#8217; because of its exponent: </p>
<pre>
You have: 8/pi^2 * lbm/ft^3 * ft * (ft^3/s)^2 /in^5
You want: psi
        * 43.533969
        / 0.022970568
</pre>
<p> Without parentheses, and using spaces for multiplication, the previous conversion would need to be entered as </p>
<pre>
You have: 8 lb ft ft^3 ft^3 / pi^2 ft^3 s^2 in^5
You want: psi
        * 43.533969
        / 0.022970568
</pre>
<h3>Backwards Compatibility:</h3>
<p> &#8216;*&#8217; and &#8216;-&#8216; The original &#8216;units&#8217; assigned multiplication a higher precedence than division using the slash. This differs from the usual precedence rules, which give multiplication and division equal precedence, and can be confusing for people who think of units as a calculator. </p>
<p> The star operator &#8216;(&#8216;* included in this &#8216;units&#8217; program has, by default, the same precedence as division, and hence follows the usual precedence rules. For backwards compatibility you can invoke &#8216;units&#8217; with the &#8216;&#8211;oldstar&#8217; option. Then &#8216;*&#8217; has a higher precedence than division, and the same precedence as multiplication using the space. </p>
<p> Historically, the hyphen &#8216;(&#8216;- has been used in technical publications to indicate products of units, and the original &#8216;units&#8217; program treated it as a multiplication operator. Because &#8216;units&#8217; provides several other ways to obtain unit products, and because &#8216;-&#8216; is a subtraction operator in general algebraic expressions, &#8216;units&#8217; treats the binary &#8216;-&#8216; as a subtraction operator by default. For backwards compatibility use the &#8216;&#8211;product&#8217; option, which causes &#8216;units&#8217; to treat the binary &#8216;-&#8216; operator as a product operator. When &#8216;-&#8216; is a multiplication operator it has the same precedence as multiplication with a space, giving it a higher precedence than division. </p>
<p> When &#8216;-&#8216; is used as a unary operator it negates its operand. Regardless of the &#8216;units&#8217; options, if &#8216;-&#8216; appears after &#8216;(&#8216; or after &#8216;+&#8217; then it will act as a negation operator. So you can always compute 20 degrees minus 12 minutes by entering &#8217;20 degrees + -12 arcmin&#8217;. You must use this construction when you define new units because you cannot know what options will be in force when your definition is processed. </p>
<h2>NONLINEAR UNIT CONVERSIONS</h2>
<p> Nonlinear units are represented using functional notation. They make possible nonlinear unit conversions such as temperature. </p>
<h3>Temperature Conversions</h3>
<p> Conversions between temperatures are different from linear conversions between temperature <i>increments</i>&#8212;see the example below. The absolute temperature conversions are handled by units starting with &#8216;temp&#8217;, and you must use functional notation. The temperature-increment conversions are done using units starting with &#8216;deg&#8217; and they do not require functional notation. </p>
<pre>
You have: tempF(45)
You want: tempC
        7.2222222
You have: 45 degF
You want: degC
        * 25
        / 0.04
</pre>
<p> Think of &#8216;tempF(<i>x</i>)&#8217; not as a function but as a notation that indicates that <i>x</i> should have units of &#8216;tempF&#8217; attached to it. See <i>Defining Nonlinear Units</i>. The first conversion shows that if it&#8217;s 45 degrees Fahrenheit outside, it&#8217;s 7.2 degrees Celsius. The second conversion indicates that a change of 45 degrees Fahrenheit corresponds to a change of 25 degrees Celsius. The conversion from &#8216;tempF(<i>x</i>)&#8217; is to absolute temperature, so that </p>
<pre>
You have: tempF(45)
You want: degR
        * 504.67
        / 0.0019814929
</pre>
<p> gives the same result as </p>
<pre>
You have: tempF(45)
You want: tempR
        * 504.67
        / 0.0019814929
</pre>
<p> But if you convert &#8216;tempF(<i>x</i>)&#8217; to &#8216;degC&#8217;, the output is probably not what you expect: </p>
<pre>
You have: tempF(45)
You want: degC
        * 280.37222
        / 0.0035666871
</pre>
<p> The result is the temperature in K, because &#8216;degC&#8217; is defined as &#8216;K&#8217;, the Kelvin. For consistent results, use the &#8216;temp<i>X</i>&#8216; units when converting to a temperature rather than converting a temperature increment. </p>
<h3>Other Nonlinear Units</h3>
<p> Some other examples of nonlinear units are numerous different ring sizes and wire gauges, the grit sizes used for abrasives, the decibel scale, shoe size, scales for the density of sugar (e.g. baume). The standard data file also supplies units for computing the area of a circle and the volume of a sphere. See the standard units data file for more details. Wire gauges with multiple zeroes are signified using negative numbers where two zeroes is &#8216;-1&#8217;. Alternatively, you can use the synonyms &#8216;g00&#8217;, &#8216;g000&#8217;, and so on that are defined in the standard units data file. </p>
<pre>
You have: wiregauge(11)
You want: inches
        * 0.090742002
        / 11.020255
You have: brwiregauge(g00)
You want: inches
        * 0.348
        / 2.8735632
You have: 1 mm
You want: wiregauge
        18.201919
You have: grit_P(600)
You want: grit_ansicoated
        342.76923
</pre>
<p> The last example shows the conversion from P graded sand paper, which is the European standard and may be marked &#8220;P600&#8221; on the back, to the USA standard. </p>
<p> You can compute the area of a circle using the nonlinear unit, &#8216;circlearea&#8217;. You can also do this using the circularinch or circleinch. The next example shows two ways to compute the area of a circle with a five inch radius and one way to compute the volume of a sphere with a radius of one meter. </p>
<pre>
You have: circlearea(5 in)
You want: in2
        * 78.539816
        / 0.012732395
You have: 10^2 circleinch
You want: in2
        * 78.539816
        / 0.012732395
You have: spherevol(meter)
You want: ft3
        * 147.92573
        / 0.0067601492
</pre>
<h2>UNIT LISTS: CONVERSION TO SUMS OF UNITS</h2>
<p> Outside of the SI, it is sometimes desirable to convert a single unit to a sum of units&#8212;for example, feet to feet plus inches. The conversion <i>from</i> sums of units was described in <i>Sums and Differences of Units</i> and is a simple matter of adding the units with the &#8216;+&#8217; sign: </p>
<pre>
You have: 12 ft + 3 in + 3|8 in
You want: ft
        * 12.28125
        / 0.081424936
</pre>
<p> Although you can similarly write a sum of units to convert <i>to</i>, the result will not be the conversion to the units in the sum, but rather the conversion to the particular sum that you have entered: </p>
<pre>
You have: 12.28125 ft
You want: ft + in + 1|8 in
        * 11.228571
        / 0.089058524
</pre>
<p> The unit expression given at the &#8216;You want:&#8217; prompt is equivalent to asking for conversion to multiples of &#8216;1 ft + 1 in + 1|8 in&#8217;, which is 1.09375 ft, so the conversion in the previous example is equivalent to </p>
<pre>
You have: 12.28125 ft
You want: 1.09375 ft
        * 11.228571
        / 0.089058524
</pre>
<p> In converting to a sum of units like miles, feet and inches, you typically want the largest integral value for the first unit, followed by the largest integral value for the next, and the remainder converted to the last unit. You can do this conversion easily with &#8216;units&#8217; using a special syntax for lists of units. You must list the desired units in order from largest to smallest, separated by the semicolon &#8216;(&#8216;; character: </p>
<pre>
You have: 12.28125 ft
You want: ft;in;1|8 in
        12 ft + 3 in + 3|8 in
</pre>
<p> The conversion always gives integer coefficients on the units in the list, except possibly the last unit when the conversion is not exact: </p>
<pre>
You have: 12.28126 ft
You want: ft;in;1|8 in
        12 ft + 3 in + 3.00096 * 1|8 in
</pre>
<p> The order in which you list the units is important: </p>
<pre>
You have: 3 kg
You want: oz;lb
        105 oz + 0.051367866 lb
You have: 3 kg
You want: lb;oz
        6 lb + 9.8218858 oz
</pre>
<p> Listing ounces before pounds produces a technically correct result, but not a very useful one. You must list the units in descending order of size in order to get the most useful result. </p>
<p> Ending a unit list with the separator &#8216;;&#8217; has the same effect as repeating the last unit on the list, so &#8216;ft;in;1|8 in;&#8217; is equivalent to &#8216;ft;in;1|8 in;1|8 in&#8217;. With the example above, this gives </p>
<pre>
You have: 12.28126 ft
You want: ft;in;1|8 in;
        12 ft + 3 in + 3|8 in + 0.00096 * 1|8 in
</pre>
<p> in effect separating the integer and fractional parts of the coefficient for the last unit. If you instead prefer to round the last coefficient to an integer you can do this with the &#8216;&#8211;round&#8217; &#8216;(&#8216;-r option. With the previous example, the result is </p>
<pre>
You have: 12.28126 ft
You want: ft;in;1|8 in
        12 ft + 3 in + 3|8 in (rounded down to nearest 1|8 in)
</pre>
<p> When you use the &#8216;-r&#8217; option, repeating the last unit on the list has no effect (e.g., &#8216;ft;in;1|8 in;1|8 in&#8217; is equivalent to &#8216;ft;in;1|8 in&#8217;), and hence neither does ending a list with a &#8216;;&#8217;. With a single unit and the &#8216;-r&#8217; option, a terminal &#8216;;&#8217; <i>does</i> have an effect: it causes &#8216;units&#8217; to treat the single unit as a list and produce a rounded value for the single unit. Without the extra &#8216;;&#8217;, the &#8216;-r&#8217; option has no effect on single unit conversions. This example shows the ouput using the &#8216;-r&#8217; option: </p>
<pre>
You have: 12.28126 ft
You want: in
        * 147.37512
        / 0.0067854058
You have: 12.28126 ft
You want: in;
        147 in (rounded down to nearest in)
</pre>
<p> Each unit that appears in the list must be conformable with the first unit on the list, and of course the listed units must also be comformable with the <i>You have</i> unit that you enter. </p>
<pre>
You have: meter
You want: ft;kg
             ^
conformability error
        ft = 0.3048 m
        kg = 1 kg
You have: meter
You want: lb;oz
conformability error
        1 m
        0.45359237 kg
</pre>
<p> In the first case, &#8216;units&#8217; reports the disagreement between units appearing on the list. In the second case, &#8216;units&#8217; reports disagreement between the unit you entered and the desired conversion. This conformability error is based on the first unit on the unit list. </p>
<p> Other common candidates for conversion to sums of units are angles and time: </p>
<pre><code>
You have : 23.437754 deg
    You want;
deg;
arcmin;
arcsec 23 deg + 26 arcmin + 15.9144 arcsec You have : 7.2319 hr You want : hr;
min;
sec 7 hr + 13 min + 54.84 sec
</code></pre>
<p> In North America, recipes for cooking typically measure ingredients by volume, and use units that are not always convenient multiples of each other. Suppose that you have a recipe for 6 and you wish to make a portion for 1. If the recipe calls for 2 1/2 cups of an ingredient, you might wish to know the measurements in terms of measuring devices you have available, you could use &#8216;units&#8217; and enter </p>
<p>You have : (2 + 1 | 2) cup / 6 You want : cup;<br />
1 | 2 cup;<br />
1 | 3 cup;<br />
1 | 4 cup;<br />
tbsp;<br />
tsp;<br />
1 | 2 tsp;<br />
1 | 4 tsp 1 | 3 cup + 1 tbsp + 1 tsp</p>
<p> By default, if a unit in a list begins with fraction of the form 1|<i>x</i> and its multiplier is an integer, the fraction is given as the product of the multiplier and the numerator; for example, </p>
<pre>
You have: 12.28125 ft
You want: ft;in;1|8 in;
        12 ft + 3 in + 3|8 in
</pre>
<p> In many cases, such as the example above, this is what is wanted, but sometimes it is not. For example, a cooking recipe for 6 might call for 5 1/4 cup of an ingredient, but you want a portion for 2, and your 1-cup measure is not available; you might try </p>
<pre>
You have: (5+1|4) cup / 3
You want: 1|2 cup;1|3 cup;1|4 cup
        3|2 cup + 1|4 cup
</pre>
<p> This result might be fine for a baker who has a 1 1/2-cup measure (and recognizes the equivalence), but it may not be as useful to someone with more limited set of measures, who does want to do additional calculations, and only wants to know &#8220;How many 1/2-cup measures to I need to add?&#8221; After all, that&#8217;s what was actually asked. With the &#8216;&#8211;show-factor&#8217; option, the factor will not be combined with a unity numerator, so that you get </p>
<pre>
You have: (5+1|4) cup / 3
You want: 1|2 cup;1|3 cup;1|4 cup
        3 * 1|2 cup + 1|4 cup
</pre>
<p> A user-specified fractional unit with a numerator other than 1 is never overridden, however&#8212;if a unit list specifies &#8216;3|4 cup;1|2 cup&#8217;, a result equivalent to 1 1/2 cups will always be shown as &#8216;2 * 3|4 cup&#8217; whether or not the &#8216;&#8211;show-factor&#8217; option is given. </p>
<p> Some applications for unit lists may be less obvious. Suppose that you have a postal scale and wish to ensure that it&#8217;s accurate at 1 oz, but have only metric calibration weights. You might try </p>
<p>You have : 1 oz<br />
    You want : 100 g;<br />
50 g;<br />
20 g;<br />
10 g;<br />
5 g;<br />
2 g;<br />
1 g;<br />
20 g + 5 g + 2 g + 1 g + 0.34952312 * 1 g</p>
<p> You might then place one each of the 20 g, 5 g, 2 g, and 1 g weights on the scale and hope that it indicates close to </p>
<pre>
You have: 20 g + 5 g + 2 g + 1 g
You want: oz;
        0.98767093 oz
</pre>
<p> Appending &#8216;;&#8217; to &#8216;oz&#8217; forces a one-line display that includes the unit; here the integer part of the result is zero, so it is not displayed. </p>
<p> A unit list such as </p>
<p>cup;<br />
1 | 2 cup;<br />
1 | 3 cup;<br />
1 | 4 cup;<br />
tbsp;<br />
tsp;<br />
1 | 2 tsp;<br />
1 | 4 tsp</p>
<p> can be tedious to enter. The &#8216;units&#8217; program provides shorthand names for some common combinations: </p>
<pre>
hms         hours, minutes, seconds                
dms         angle: degrees, minutes, seconds       
time        years, days, hours, minutes and seconds
usvol       US cooking volume: cups and smaller    
</pre>
<p> Using these shorthands, or <i>unit list aliases</i>, you can do the following conversions: </p>
<pre>
You have: anomalisticyear 
You want: time
        1 year + 25 min + 3.4653216 sec
You have: 1|6 cup
You want: usvol
        2 tbsp + 2 tsp
</pre>
<p> You cannot combine a unit list alias with other units: it must appear alone at the &#8216;You want:&#8217; prompt. </p>
<p> You can display the definition of a unit list alias by entering it at the &#8216;You have:&#8217; prompt: </p>
<pre>
You have: dms
        Definition: unit list, deg;arcmin;arcsec
</pre>
<p> When you specify compact output with &#8216;&#8211;compact&#8217;, &#8216;&#8211;terse&#8217; or &#8216;-t&#8217; and perform conversion to a unit list, &#8216;units&#8217; lists the conversion factors for each unit in the list, separated by semicolons. </p>
<pre>
You have: year
You want: day;min;sec
365;348;45.974678
</pre>
<p> Unlike the case of regular output, zeros <i>are</i> included in this output list: </p>
<p>You have : liter<br />
               You want : cup;<br />
1 | 2 cup;<br />
1 | 4 cup;<br />
tbsp 4;<br />
0;<br />
0;<br />
3.6280454</p>
<h2>INVOKING UNITS</h2>
<p> You invoke &#8216;units&#8217; like this: </p>
<p>units[options][from &#8211; unit[to &#8211; unit]]</p>
<p> If the <i>from-unit</i> and <i>to-unit</i> are omitted, then the program will use interactive prompts to determine which conversions to perform. See <i>Interactive Use</i>. If both <i>from-unit</i> and <i>to-unit</i> are given, &#8216;units&#8217; will print the result of that single conversion and then exit. If only <i>from-unit</i> appears on the command line, &#8216;units&#8217; will display the definition of that unit and exit. Units specified on the command line may need to be quoted to protect them from shell interpretation and to group them into two arguments. See <i>Command Line Use</i>. </p>
<p> The following options allow you to read in an alternative units file, check your units file, or change the output format: </p>
<dl>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd> Check that all units and prefixes defined in the units data file reduce to primitive units. Print a list of all units that cannot be reduced. Also display some other diagnostics about suspicious definitions in the units data file. Only definitions active in the current locale are checked. You should always run &#8216;units&#8217; with this option after modifying a units data file.</dl>
<dl>
<dt><code>&#8211;check-verbose</code>, <code>&#8211;verbose-check</code></p>
<dd> Like the &#8216;&#8211;check&#8217; option, this option prints a list of units that cannot be reduced. But to help find unit definitions that cause endless loops, it lists the units as they are checked. If &#8216;units&#8217; hangs, then the last unit to be printed has a bad definition. Only definitions active in the current locale are checked.</dl>
<dl>
<dt><code>-o </code><i>format</i>, <code>&#8211;output-format </code><i>format</i></p>
<dd> Use the specified <i>format</i> for numeric output; the format is a subset of that for the printf function in the ANSI C standard. Only a numeric format &#8216;(&#8216;E or &#8216;e&#8217; for scientific notation, &#8216;f&#8217; for fixed-point decimal, or &#8216;G&#8217; or &#8216;g&#8217; to specify the number of significant figures) is allowed. The default format is &#8216;%.8g&#8217;; for greater precision, you could specify &#8216;-o %.15g&#8217;. See <i>Numeric Output Format</i> and the documentation for printf() for more detailed descriptions of the format specification.</dl>
<dl>
<dt><code>-e</code>, <code>&#8211;exponential</code></p>
<dd> Set the numeric output format to exponential (i.e., scientific notation), like that used in the Unix &#8216;units&#8217; program.</dl>
<dl>
<dt><code>-f </code><i>filename</i>, <code>&#8211;file </code><i>filename</i></p>
<dd> Instruct &#8216;units&#8217; to load the units file &#8216;filename&#8217;. You can specify up to 25 units files on the command line. When you use this option, &#8216;units&#8217; will load <i>only</i> the files you list on the command line; it will not load the standard file or your personal units file unless you explicitly list them. If <i>filename</i> is the empty string &#8216;(&#8216;-f &quot;&quot; the default units file (or that specified by &#8216;UNITSFILE&#8217;) will be loaded in addition to any others specified with &#8216;-f&#8217;.</dl>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print out a summary of the options for &#8216;units&#8217;.</dl>
<dl>
<dt><code>-m</code>, <code>&#8211;minus</code></p>
<dd> Causes &#8216;-&#8216; to be interpreted as a subtraction operator. This is the default behavior.</dl>
<dl>
<dt><code>-p</code>, <code>&#8211;product</code></p>
<dd> Causes &#8216;-&#8216; to be interpreted as a multiplication operator when it has two operands. It will act as a negation operator when it has only one operand: &#8216;(-3)&#8217;. By default &#8216;-&#8216; is treated as a subtraction operator.</dl>
<dl>
<dt><code>&#8211;oldstar</code></p>
<dd> Causes &#8216;*&#8217; to have the old-style precedence, higher than the precedence of division so that &#8216;1/2*3&#8217; will equal &#8216;1/6&#8217;.</dl>
<dl>
<dt><code>&#8211;newstar</code></p>
<dd> Forces &#8216;*&#8217; to have the new (default) precedence that follows the usual rules of algebra: the precedence of &#8216;*&#8217; is the same as the precedence of &#8216;/&#8217;, so that &#8216;1/2*3&#8217; will equal &#8216;3/2&#8217;.</dl>
<dl>
<dt><code>&#8211;compact</code></p>
<dd> Give compact output featuring only the conversion factor. This turns off the &#8216;&#8211;verbose&#8217; option.</dl>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> Suppress prompting of the user for units and the display of statistics about the number of units loaded.</dl>
<dl>
<dt><code>-n</code>, <code>&#8211;nolists</code></p>
<dd> Disable conversion to unit lists.</dl>
<dl>
<dt><code>-r</code>, <code>&#8211;round</code></p>
<dd> When converting to a combination of units given by a unit list, round the value of the last unit in the list to the nearest integer.</dl>
<dl>
<dt><code>-S</code>, <code>&#8211;show-factor</code></p>
<dd> When converting to a combination of units specified in a list, always show a non-unity factor before a unit that begins with a fraction with a unity denominator. By default, if the unit in a list begins with fraction of the form 1|<i>x</i> and its multiplier is an integer other than 1, the fraction is given as the product of the multiplier and the numerator (e.g., &#8216;3|8 in&#8217; rather than &#8216;3 * 1|8 in&#8217;). In some cases, this is not what is wanted; for example, the results for a cooking recipe might show &#8216;3 * 1|2 cup&#8217; as &#8216;3|2 cup&#8217;. With the &#8216;&#8211;show-factor&#8217; option, a result equivalent to 1.5 cups will display as &#8216;3 * 1|2 cup&#8217; rather than &#8216;3|2 cup&#8217;. A user-specified fractional unit with a numerator other than 1 is never overridden, however&#8212;if a unit list specifies &#8216;3|4 cup;1|2 cup&#8217;, a result equivalent to 1 1/2 cups will always be shown as &#8216;2 * 3|4 cup&#8217; whether or not the &#8216;&#8211;show-factor&#8217; option is given.</dl>
<dl>
<dt><code>-s</code>, <code>&#8211;strict</code></p>
<dd> Suppress conversion of units to their reciprocal units. For example, &#8216;units&#8217; will normally convert hertz to seconds because these units are reciprocals of each other. The strict option requires that units be strictly conformable to perform a conversion, and will give an error if you attempt to convert hertz to seconds.</dl>
<dl>
<dt><code>-1</code>, <code>&#8211;one-line</code></p>
<dd> Give only one line of output (the forward conversion). Do not print the reverse conversion. If a reciprocal conversion is performed then &#8216;units&#8217; will still print the &#8220;reciprocal conversion&#8221; line.</dl>
<dl>
<dt><code>-t</code>, <code>&#8211;terse</code></p>
<dd> Give terse output when converting units. This option can be used when calling &#8216;units&#8217; from another program so that the output is easy to parse. This option has the combined effect of these options: &#8216;&#8211;strict&#8217; &#8216;&#8211;quiet&#8217; &#8216;&#8211;one-line&#8217; &#8216;&#8211;compact&#8217;.</dl>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Give slightly more verbose output when converting units. When combined with the &#8216;-c&#8217; option this gives the same effect as &#8216;&#8211;check-verbose&#8217;.</dl>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print program version number, tell whether the &#8216;readline&#8217; library has been included, and give the location of the default units data file.</dl>
<dl>
<dt><code>-l </code><i>locale</i>, <code>&#8211;locale </code><i>locale</i></p>
<dd> Force a specified locale such as &#8216;en_GB&#8217; to get British definitions by default. This overrides the locale determined from system settings or environment variables. See <i>Locale</i> for a description of locale format.</dl>
<h2>ADDING YOUR OWN DEFINITIONS</h2>
<h3>Units Data Files</h3>
<p> The units and prefixes that &#8216;units&#8217; can convert are defined in the units data file, typically &#8216;/usr/share/units/definitions.units&#8217;. Although you can extend or modify this data file if you have appropriate user privileges, it&#8217;s usually better to put extensions in separate files so that the definitions will be preserved when you update &#8216;units&#8217;. </p>
<p> You can include additional data files in the units database using the &#8216;!include&#8217; command in the standard units data file. For example </p>
<pre>
!include    /usr/local/share/units/local.units
</pre>
<p> might be appropriate for a site-wide supplemental data file. The location of the &#8216;!include&#8217; statement in the standard units data file is important; later definitions replace earlier ones, so any definitions in an included file will override definitions before the &#8216;!include&#8217; statement in the standard units data file. With normal invocation, no warning is given about redefinitions; to ensure that you don&#8217;t have an unintended redefinition, run &#8216;units -c&#8217; after making changes to any units data file. </p>
<p> If you want to add your own units in addition to or in place of standard or site-wide supplemental units data files, you can include them in the &#8216;.units&#8217; file in your home directory. If this file exists it is read after the standard units data file, so that any definitions in this file will replace definitions of the same units in the standard data file or in files included from the standard data file. This file will not be read if any units files are specified on the command line. (Under Windows the personal units file is named &#8216;unitdef.units&#8217;.) </p>
<p> The &#8216;units&#8217; program first tries to determine your home directory from the &#8216;HOME&#8217; environment variable. On systems running Microsoft Windows, if &#8216;HOME&#8217; does not exist, &#8216;units&#8217; attempts to find your home directory from &#8216;HOMEDRIVE&#8217; and &#8216;HOMEPATH&#8217;. Running &#8216;units -V&#8217; will display the location and name of your personal units file. </p>
<p> You can specify an arbitrary file as your personal units data file with the &#8216;MYUNITSFILE&#8217; environment variable; if this variable exists, its value is used without searching your home directory. </p>
<h3>Defining New Units and Prefixes</h3>
<p> A unit is specified on a single line by giving its name and an equivalence. Comments start with a &#8216;#&#8217; character, which can appear anywhere in a line. The backslash character &#8216;(&#8216;\ acts as a continuation character if it appears as the last character on a line, making it possible to spread definitions out over several lines if desired. A file can be included by giving the command &#8216;!include&#8217; followed by the file&#8217;s name. The &#8216;!&#8217; must be the first character on the line. The file will be sought in the same directory as the parent file unless you give a full path. The name of the file to be included cannot contain the comment character &#8216;#&#8217;. </p>
<p> Unit names must not contain any of the operator characters &#8216;+&#8217;, &#8216;-&#8216;, &#8216;*&#8217;, &#8216;/&#8217;, &#8216;|&#8217;, &#8216;^&#8217;, &#8216;;&#8217;, &#8216;~&#8217;, the comment character &#8216;#&#8217;, or parentheses. They cannot begin or end with an underscore &#8216;(&#8216;_ a comma &#8216;(&#8216;, or a decimal point &#8216;(&#8216;. Names cannot begin with a digit, and if a name ends in a digit other than zero, the digit must be preceded by a string beginning with an underscore, and afterwards consisting only of digits, decimal points, or commas. For example, &#8216;foo_2&#8217;, &#8216;foo_2,1&#8217;, or &#8216;foo_3.14&#8217; would be valid names but &#8216;foo2&#8217; or &#8216;foo_a2&#8217; would be invalid. You could define nitrous oxide as </p>
<pre>
N2O     nitrogen 2  + oxygen
</pre>
<p> but would need to define nitrogen dioxide as </p>
<pre>
NO_2    nitrogen + oxygen 2
</pre>
<p> Be careful to define new units in terms of old ones so that a reduction leads to the primitive units, which are marked with &#8216;!&#8217; characters. Dimensionless units are indicated by using the string &#8216;!dimensionless&#8217; for the unit definition. </p>
<p> When adding new units, be sure to use the &#8216;-c&#8217; option to check that the new units reduce properly. If you create a loop in the units definitions, then &#8216;units&#8217; will hang when invoked with the &#8216;-c&#8217; option. You will need to use the &#8216;&#8211;check-verbose&#8217; option, which prints out each unit as it is checked. The program will still hang, but the last unit printed will be the unit that caused the infinite loop. </p>
<p> If you define any units that contain &#8216;+&#8217; characters, carefully check them because the &#8216;-c&#8217; option will not catch non-conformable sums. Be careful with the &#8216;-&#8216; operator as well. When used as a binary operator, the &#8216;-&#8216; character can perform addition or multiplication depending on the options used to invoke &#8216;units&#8217;. To ensure consistent behavior use &#8216;-&#8216; only as a unary negation operator when writing units definitions. To multiply two units leave a space or use the &#8216;*&#8217; operator with care, recalling that it has two possible precedence values and may require parentheses to ensure consistent behavior. To compute the difference of &#8216;foo&#8217; and &#8216;bar&#8217; write &#8216;foo+(-bar)&#8217; or even &#8216;foo+-bar&#8217;. </p>
<p> Here is an example of a short data file that defines some basic units: </p>
<pre>
m       !               # The meter is a primitive unit
sec     !               # The second is a primitive unit
rad     !dimensionless  # A dimensionless primitive unit
micro-  1e-6            # Define a prefix
minute  60 sec          # A minute is 60 seconds
hour    60 min          # An hour is 60 minutes
inch    0.0254 m        # Inch defined in terms of meters
ft      12 inches       # The foot defined in terms of inches
mile    5280 ft         # And the mile
</pre>
<p> A unit that ends with a &#8216;-&#8216; character is a prefix. If a prefix definition contains any &#8216;/&#8217; characters, be sure they are protected by parentheses. If you define &#8216;half- 1/2&#8217; then &#8216;halfmeter&#8217; would be equivalent to &#8216;1 / (2 meter)&#8217;. </p>
<h3>Defining Nonlinear Units</h3>
<p> Some unit conversions of interest are nonlinear; for example, temperature conversions between the Fahrenheit and Celsius scales cannot be done by simply multiplying by conversion factors. </p>
<p> When you give a linear unit definition such as &#8216;inch 2.54 cm&#8217; you are providing information that &#8216;units&#8217; uses to convert values in inches into primitive units of meters. For nonlinear units, you give a functional definition that provides the same information. </p>
<p> Nonlinear units are represented using a functional notation. It is best to regard this notation not as a function call but as a way of adding units to a number, much the same way that writing a linear unit name after a number adds units to that number. Internally, nonlinear units are defined by a pair of functions that convert to and from linear units in the data file, so that an eventual conversion to primitive units is possible. </p>
<p> Here is an example nonlinear unit definition: </p>
<pre>
tempF(x) units=[1;K] (x+(-32)) degF + stdtemp ; \
                     (tempF+(-stdtemp))/degF + 32
</pre>
<p> A nonlinear unit definition comprises a unit name, a dummy parameter name, two functions, and two corresponding units. The functions tell &#8216;units&#8217; how to convert to and from the new unit. In order to produce valid results, the arguments of these functions need to have the correct dimensions. To facilitate error checking, you may optionally indicate units for these arguments. </p>
<p> The definition begins with the unit name followed immediately (with no spaces) by a &#8216;(&#8216; character. In parentheses is the name of the parameter. Next is an optional specification of the units required by the functions in this definition. In the example above, the &#8216;tempF&#8217; function requires an input argument conformable with &#8216;1&#8217;. For normal nonlinear units definitions the forward function will always take a dimensionless argument. The inverse function requires an input argument conformable with &#8216;K&#8217;. In general the inverse function will need units that match the quantity measured by your nonlinear unit. The purpose of the expression in brackets to enable &#8216;units&#8217; to perform error checking on function arguments, and also to assign units to range and domain specifications, which are described later. </p>
<p> Next the function definitions appear. In the example above, the &#8216;tempF&#8217; function is defined by </p>
<pre>
tempF(x) = (x+(-32)) degF + stdtemp
</pre>
<p> This gives a rule for converting &#8216;x&#8217; in the units &#8216;tempF&#8217; to linear units of absolute temperature, which makes it possible to convert from tempF to other units. </p>
<p> In order to make conversions to Fahrenheit possible, you must give a rule for the inverse conversions. The inverse will be &#8216;x(tempF)&#8217; and its definition appears after a &#8216;;&#8217; character. In our example, the inverse is </p>
<pre>
x(tempF) = (tempF+(-stdtemp))/degF + 32
</pre>
<p> This inverse definition takes an absolute temperature as its argument and converts it to the Fahrenheit temperature. The inverse can be omitted by leaving out the &#8216;;&#8217; character, but then conversions to the unit will be impossible. If the inverse is omitted then the &#8216;&#8211;check&#8217; option will display a warning. It is up to you to calculate and enter the correct inverse function to obtain proper conversions. The &#8216;&#8211;check&#8217; option tests the inverse at one point and prints an error if it is not valid there, but this is not a guarantee that your inverse is correct. </p>
<p> If you wish to make synonyms for nonlinear units, you still need to define both the forward and inverse functions. Inverse functions can be obtained using the &#8216;~&#8217; operator. So to create a synonym for &#8216;tempF&#8217; you could write </p>
<p>fahrenheit(x) units = [1; K] tempF(x);<br />
~tempF(fahrenheit)</p>
<p> You may define a function whose range and domain do not cover all of the real numbers. In this case &#8216;units&#8217; can handle errors better if you specify an appropriate range and domain. You specify the range and domain as shown below. </p>
<p>baume(d) units = [1; g / cm ^ 3] domain = [ 0, 130.5 ] range = [ 1, 10 ](145 / (145 &#8211; d)) g / cm ^ 3;<br />
(baume + -g / cm ^ 3)145 / baume</p>
<p> In this example the domain is specified after the &#8216;domain=&#8217; with the endpoints given in brackets. One of the end points can be omitted to get an interval that goes to infinity. So the range could be specified as nonnegative by writing &#8216;range=[0,]&#8217;. Both the range and domain are optional and can appear independently and in any order along with the &#8216;units&#8217; specification. The values in the range and domain are attached to the units given in the &#8216;units&#8217; specification. If you don&#8217;t specify the units then the parameter inputs are reduced to primitive units for the numeric comparison to the values you give in the range or domain. In this case you should only use &#8216;range&#8217; or &#8216;domain&#8217; if the endpoints are zero and infinity. </p>
<p> Specifying the range and domain allows &#8216;units&#8217; to perform better error checking and give more helpful error messages when you invoke nonlinear units conversions outside of their bounds. It also enables the &#8216;-c&#8217; option to find a point in the domain to use for its point check of your inverse definition. </p>
<p> You may occasionally wish to define a function that operates on units. This can be done using a nonlinear unit definition. For example, the definition below provides conversion between radius and the area of a circle. This definition requires a length as input and produces an area as output, as indicated by the &#8216;units=&#8217; specification. Specifying the range as the nonnegative numbers can prevent cryptic error messages. </p>
<pre>
circlearea(r) units=[m;m^2] range=[0,]   pi r^2 ; sqrt(circlearea/pi)
</pre>
<p> Sometimes you may be interested in a piecewise linear unit such as many wire gauges. Piecewise linear units can be defined by specifying conversions to linear units on a list of points. Conversion at other points will be done by linear interpolation. A partial definition of zinc gauge is </p>
<pre>
zincgauge[in] 1 0.002, 10 0.02, 15 0.04, 19 0.06, 23 0.1
</pre>
<p> In this example, &#8216;zincgauge&#8217; is the name of the piecewise linear unit. The definition of such a unit is indicated by the embedded &#8216;[&#8216; character. After the bracket, you should indicate the units to be attached to the numbers in the table. No spaces can appear before the &#8216;]&#8217; character, so a definition like &#8216;foo[kg meters]&#8217; is illegal; instead write &#8216;foo[kg*meters]&#8217;. The definition of the unit consists of a list of pairs optionally separated by commas. This list defines a function for converting from the piecewise linear unit to linear units. The first item in each pair is the function argument; the second item is the value of the function at that argument (in the units specified in brackets). In this example, we define &#8216;zincgauge&#8217; at five points. For example, we set &#8216;<a href="/docs/linux/man/1-zincgauge/">zincgauge</a>(1)&#8217; equal to &#8216;0.002 in&#8217;. Definitions like this may be more readable if written using continuation characters as </p>
<pre>
zincgauge[in] \
     1 0.002  \
    10 0.02   \
    15 0.04   \
    19 0.06   \
    23 0.1
</pre>
<p> With the preceding definition, the following conversion can be performed: </p>
<pre>
You have: zincgauge(10)
You want: in
    * 0.02
    / 50
You have: .01 inch
You want: zincgauge
    5
</pre>
<p> If you define a piecewise linear unit that is not strictly monotonic, then the inverse will not be well defined. If the inverse is requested for such a unit, &#8216;units&#8217; will return the smallest inverse. The &#8216;&#8211;check&#8217; option will print a warning if a non-monotonic piecewise linear unit is encountered. </p>
<h3>Defining Unit List Aliases</h3>
<p> Unit list aliases are treated differently from unit definitions, because they are a data entry shorthand rather than a true definition for a new unit. A unit list alias definition begins with &#8216;!unitlist&#8217; and includes the alias and the definition; for example, the aliases included in the standard units data file are </p>
<pre><code>
!unitlist hms hr;
min;
sec !unitlist time year;
day;
hr;
min;
sec !unitlist dms deg;
arcmin;
arcsec !unitlist ftin ft;
in;
1 | 8 in !unitlist usvol cup;
3 | 4 cup;
2 | 3 cup;
1 | 2 cup;
1 | 3 cup;
1 | 4 cup;
tbsp;
tsp;
1 | 2 tsp;
1 | 4 tsp;
1 | 8 tsp
</code></pre>
<p> Unit list aliases are only for unit lists, so the definition must include a &#8216;;&#8217;. Unit list aliases can never be combined with units or other unit list aliases, so the definition of &#8216;time&#8217; shown above could <i>not</i> have been shortened to &#8216;year;day;hms&#8217;. As usual, be sure to run &#8216;units &#8211;check&#8217; to ensure that the units listed in unit list aliases are conformable. </p>
<h2>NUMERIC OUTPUT FORMAT</h2>
<p> By default, results of conversions are shown to eight significant figures; this can be changed with the &#8216;&#8211;exponential&#8217; and &#8216;&#8211;output-format&#8217; options. The former sets an exponential format (i.e., scientific notation) like that used in the original Unix &#8216;units&#8217; program; the latter allows the format to be given as that of the printf function in the ANSI C standard. </p>
<p> The format recognized with the &#8216;&#8211;output-format&#8217; option is a subset of that for printf(). Only a floating-point format of the form &#8216;%'[<i>flag</i>][<i>width</i>][ &#8216;.&#8217;<i>precision</i>]<i>type</i> is allowed: it must begin with &#8216;%&#8217;, and must end with a floating-point type specifier &#8216;(&#8216;E or &#8216;e&#8217; for scientific notation, &#8216;f&#8217; for fixed-point decimal, or &#8216;G&#8217; or &#8216;g&#8217; to specify the number of significant figures). The format specification may include one optional flag &#8216;(&#8216;+ &#8216;-&#8216;, &#8216;#&#8217;, or a space), followed by an optional value for the minimum field width, and an optional precision specification that begins with a period (e.g., &#8216;.6&#8217;). In addition to the digits, the field width includes the decimal point, the exponent, and the sign if any of these are shown. A width specification is typically used with fixed-point decimal to have columns of numbers align at the decimal point; it normally is not useful with &#8216;units&#8217;. Non-floating-point type specifiers make no sense for &#8216;units&#8217;, and are forbidden. </p>
<p> The default format is &#8216;%.8g&#8217;; for greater precision, you could specify &#8216;-o %.15g&#8217;. The &#8216;G&#8217; and &#8216;g&#8217; formats use exponential format whenever the exponent would be less than -5, so the value 0.000013 displays as &#8216;1.3e-005&#8217;. If you prefer fixed-point display, you might specify &#8216;-o %.8f&#8217;; however, very small numbers may display very few significant figures, and for very small numbers, may show nothing but zeros. </p>
<p> See the documentation for printf() for more detailed descriptions of the format specification. </p>
<h2>LOCALIZATION</h2>
<p> Some units have different values in different locations. The localization feature accommodates this by allowing a units data file to specify definitions that depend on the user&#8217;s locale. </p>
<h3>Locale</h3>
<p> A locale is a subset of a user&#8217;s environment that indicates the user&#8217;s language and country, and some attendant preferences, such as the formatting of dates. The &#8216;units&#8217; program attempts to determine the locale from the POSIX setlocale function; if this cannot be done, &#8216;units&#8217; examines the environment variables &#8216;LC_CTYPE&#8217; and &#8216;LANG&#8217;. On POSIX systems, a locale is of the form &#8216;<i>language</i>&#8216;_ where <i>language</i> is the two-character code from ISO 639-1 and <i>country</i> is the two-character code from ISO 3166-1; <i>language</i> is lower case and <i>country</i> is upper case. For example, the POSIX locale for the United Kingdom is &#8216;en_GB&#8217;. </p>
<p> On systems running Microsoft Windows, the value returned by setlocale() is different from that on POSIX systems; &#8216;units&#8217; attempts to map the Windows value to a POSIX value by means of a table in the file &#8216;locale.map&#8217; in the same directory, typically &#8216;/usr/local/share/units&#8217;, as the default units data files. The file includes entries for many combinations of language and country, and can be extended to include other combinations. The &#8216;locale.map&#8217; comprises two tab-separated columns; each entry is of the form </p>
<pre>
<i>Windows-locale</i>   <i>POSIX-locale</i>
</pre>
<p> where <i>POSIX-locale</i> is as described above, and <i>Windows-locale</i> typically spells out both the language and country. For example, the entry for the United States is </p>
<pre>
English_United States   en_US
</pre>
<p> You can force &#8216;units&#8217; to run in a desired locale by using the &#8216;-l&#8217; option. </p>
<p> In order to create unit definitions for a particular locale you begin a block of definitions in a unit datafile with &#8216;!locale&#8217; followed by a locale name. The &#8216;!&#8217; must be the first character on the line. The &#8216;units&#8217; program reads the following definitions only if the current locale matches. You end the block of localized units with &#8216;!endlocale&#8217;. Here is an example, which defines the British gallon. </p>
<pre>
!locale en_GB
gallon       4.54609 liter
!endlocale
</pre>
<h3>Additional Localization</h3>
<p> Sometimes the locale isn&#8217;t sufficient to determine unit preferences. There could be regional preferences, or a company could have specific preferences. Though probably uncommon, such differences could arise with the choice of English customary units outside of English-speaking countries. To address this, &#8216;units&#8217; allows specifying definitions that depend on environment variable settings. The environment variables can be controled based on the current locale, or the user can set them to force a particular group of definitions. </p>
<p> A conditional block of definitions in a units data file begins with either &#8216;!var&#8217; or &#8216;!varnot&#8217; following by an environment variable name and then a space separated list of values. The leading &#8216;!&#8217; must appear in the first column of a units data file, and the conditional block is terminated by &#8216;!endvar&#8217;. Definitions in blocks beginning with &#8216;!var&#8217; are executed only if the environment variable is exactly equal to one of the listed values. Definitions in blocks beginning with &#8216;!varnot&#8217; are executed only if the environment variable does <i>not</i> equal any of the list values. </p>
<p> The inch has long been a customary measure of length in many places. The word comes from the latin <i>uncia</i> meaning &#8220;one twelfth,&#8221; referring to its relationship with the foot. By the 20th century, the inch was officially defined in English-speaking countries relative to the yard, but until 1959, the yard differed slightly among those countries. In France the customary inch, which was displaced in 1799 by the meter, had a different length based on a french foot. These customary definitions could be accomodated as follows: </p>
<pre>
!var INCH_UNIT usa 
yard          3600|3937 m
!endvar
!var INCH_UNIT canada
yard          0.9144 meter
!endvar
!var INCH_UNIT uk
yard          0.91439841 meter
!endvar
!var INCH_UNIT canada uk usa
foot          1|3 yard
inch          1|12 foot
!endvar
!var INCH_UNIT france
foot          144|443.296 m
inch          1|12 foot
line          1|12 inch
!endvar
!varnot INCH_UNIT usa uk france canada
!message Unknown value for INCH_UNIT
!endvar
</pre>
<p> When &#8216;units&#8217; reads the above definitions it will check the environment variable &#8216;INCH_UNIT&#8217; and load only the definitions for the appropriate section. If &#8216;INCH_UNIT&#8217; is unset or is not set to one of the four values listed then &#8216;units&#8217; will run the last block. In this case that block uses the &#8216;!message&#8217; command to display a warning message. Alternatively that block could set default values. </p>
<p> In order to create default values that are overridden by user settings the data file can use the &#8216;!set&#8217; command, which sets an environment variable <i>only if it is not already set</i>; these settings are only for the current &#8216;units&#8217; invocation and do not persist. So if the example above were preceded by &#8216;!set INCH_UNIT france&#8217; then this would make &#8216;france&#8217; the default value for &#8216;INCH_UNIT&#8217;. If the user had set the variable in the environment before invoking &#8216;units&#8217;, then &#8216;units&#8217; would use the user&#8217;s value. </p>
<p> To link these settings to the user&#8217;s locale you combine the &#8216;!set&#8217; command with the &#8216;!locale&#8217; command. If you wanted to combine the above example with suitable locales you could do by <i>preceding</i> the above definition with the following: </p>
<pre>
!locale en_US
!set INCH_UNIT usa
!endlocale
!locale en_GB
!set INCH_UNIT uk
!endlocale
!locale en_CA
!set INCH_UNIT canada
!endlocale
!locale fr_FR
!set INCH_UNIT france
!endlocale
!set INCH_UNIT france
</pre>
<p> These definitions set the overall default for &#8216;INCH_UNIT&#8217; to &#8216;france&#8217; and set default values for four locales appropriately. The overall default setting comes last so that it only applies when &#8216;INCH_UNIT&#8217; was not set by one of the other commands or by the user. </p>
<p> If the variable given after &#8216;!var&#8217; or &#8216;!varnot&#8217; is undefined then &#8216;units&#8217; prints an error message and ignores the definitions that follow. Use &#8216;!set&#8217; to create defaults to prevent this situation from arising. The &#8216;-c&#8217; option only checks the definitions that are active for the current environment and locale, so when adding new definitions take care to check that all cases give rise to a well defined set of definitions. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The &#8216;units&#8217; program uses the following environment variables: </p>
<dl>
<dt><code>HOME</code></p>
<dd> Specifies the location of your home directory; it is used by &#8216;units&#8217; to find a personal units data file &#8216;.units&#8217;. On systems running Microsoft Windows, &#8216;units&#8217; tries to determine your home directory from the &#8216;HOMEDRIVE&#8217; and &#8216;HOMEPATH&#8217; environment variables if &#8216;HOME&#8217; does not exist.</dl>
<dl>
<dt><code>LC_CTYPE, LANG</code></p>
<dd> Checked to determine the locale if &#8216;units&#8217; cannot obtain it from the operating system. Sections of the standard units data file are specific to certain locales.</dl>
<dl>
<dt><code>MYUNITSFILE</code></p>
<dd> Specifies your personal units data file. If this variable exists, &#8216;units&#8217; uses its value rather than searching your home directory for &#8216;.units&#8217;. The personal units file will not be loaded if any data files are given using the &#8216;-f&#8217; option.</dl>
<dl>
<dt><code>PAGER</code></p>
<dd> Specifies the pager to use for help and for displaying the conformable units. The help function browses the units database and calls the pager using the &#8216;+n&#8217;<i>n</i> syntax for specifying a line number. The default pager is &#8216;more&#8217;; &#8216;PAGER&#8217; can be used to specify alternatives such as &#8216;less&#8217;, &#8216;pg&#8217;, &#8217;emacs&#8217;, or &#8216;vi&#8217;.</dl>
<dl>
<dt><code>UNITS_ENGLISH</code></p>
<dd> Set to either &#8216;US&#8217; or &#8216;GB&#8217; to choose United States or British volume definitions, overriding the default from your locale.</dl>
<dl>
<dt><code>UNITSFILE</code></p>
<dd> Specifies the units data file to use (instead of the default). You can only specify a single units data file using this environment variable. If units data files are given using the &#8216;-f&#8217; option, the file specified by &#8216;UNITSFILE&#8217; will be not be loaded unless the &#8216;-f&#8217; option is given with the empty string &#8216;(&#8216;units -f&nbsp;<wbr>&quot;&quot;</dl>
<h2>UNICODE SUPPORT</h2>
<p> The standard units data file is written in Unicode using the UTF-8 encoding. Portions of the file that are not plain ASCII begin with &#8216;!utf8&#8217; and end with &#8216;!endutf8&#8217;. As usual, the &#8216;!&#8217; must appear as the first character on the line. If a line of a data file contains byte sequences that are invalid UTF-8 or non-printing UTF-8 then &#8216;units&#8217; ignores the entire line. </p>
<p> When &#8216;units&#8217; runs it checks the locale to determine the character set. If UTF-8 is listed, then &#8216;units&#8217; reads the utf8 definitions. If any other character set is in use, then &#8216;units&#8217; works in plain ASCII without support for extended characters. </p>
<h2>READLINE SUPPORT</h2>
<p> If the &#8216;readline&#8217; package has been compiled in, then when &#8216;units&#8217; is used interactively, numerous command line editing features are available. To check if your version of &#8216;units&#8217; includes &#8216;readline&#8217;, invoke the program with the &#8216;&#8211;version&#8217; option. </p>
<p> For complete information about &#8216;readline&#8217;, consult the documentation for the &#8216;readline&#8217; package. Without any configuration, &#8216;units&#8217; will allow editing in the style of emacs. Of particular use with &#8216;units&#8217; are the completion commands. </p>
<p> If you type a few characters and then hit <i>ESC</i> followed by &#8216;<i>?</i>&#8216; then &#8216;units&#8217; will display a list of all the units that start with the characters typed. For example, if you type &#8216;<i>metr</i>&#8216; and then request completion, you will see something like this: </p>
<pre>
You have: metr
metre             metriccup         metrichorsepower  metrictenth
metretes          metricfifth       metricounce       metricton
metriccarat       metricgrain       metricquart       metricyarncount
You have: metr
</pre>
<p> If there is a unique way to complete a unitname, you can hit the <i>TAB</i> key and &#8216;units&#8217; will provide the rest of the unit name. If &#8216;units&#8217; beeps, it means that there is no unique completion. Pressing the <i>TAB</i> key a second time will print the list of all completions. </p>
<h2>UPDATING CURRENCY EXCHANGE RATES</h2>
<p> The units program includes currency exchange rates and prices for some precious metals in the database. Of course, these values change over time, sometimes very rapidly, and &#8216;units&#8217; cannot provide real time values. To update the exchange rates run the &#8216;units_cur&#8217;, which rewrites the files containing the currency rates, typically &#8216;/usr/local/share/units/currency.units&#8217;. This program must be run with suitable permissions to write the file. To keep the rates updated automatically, it could be run by a cron job on a Unix-like system, or a similar scheduling program on a different system. Currency exchange rates are taken from Time Genie (<a rel="nofollow" href="http://www.timegenie.com)">http://www.timegenie.com)</a> and precious metals pricing from Packetizer (<a rel="nofollow" href="http://www.packetizer.com">www.packetizer.com</a>). These sites update once per day, so there is no benefit in running the update script more often than daily. You can run &#8216;units_cur&#8217; with a filename specified on the command line and it will write the data to that file. If you give &#8216;-&#8216; for the file it will write to standard output. </p>
<h2>DATABASE COMMAND SYNTAX</h2>
<dl>
<dt><i>unit</i> <i>definition</i></p>
<dd> Define a regular unit.</dl>
<dl>
<dt><i>prefix</i>&#8211; <i>definition</i></p>
<dd> Define a prefix.</dl>
<dl>
<dt><i>funcname</i>(<i>var</i>) units=[<i>in-units</i>,<i>out-units</i>] domain=[<i>x1</i>,<i>x2</i>] range=[<i>y1</i>,<i>y2</i>] <i>definition(var)</i> ; <i>inverse(funcname)</i></p>
<dd> Define a nonlinear unit or unit function. The three optional keywords &#8216;units=&#8217;, &#8216;range=&#8217; and &#8216;domain=&#8217; can appear in any order. The definition of the inverse is optional.</dl>
<dl>
<dt><i>tabname</i>[<i>out-units</i>] <i>pair-list</i></p>
<dd> Define a piecewise linear unit. The pair list gives the points on the table listed in ascending order.</dl>
<dl>
<dt><code>!endlocale</code></p>
<dd> End a block of definitions beginning with &#8216;!locale&#8217;</dl>
<dl>
<dt><code>!endutf8</code></p>
<dd> End a block of definitions begun with &#8216;!utf8&#8217;</dl>
<dl>
<dt><code>!endvar</code></p>
<dd> End a block of definitions begun with &#8216;!var&#8217; or &#8216;!varnot&#8217;</dl>
<dl>
<dt><code>!include </code><i>file</i></p>
<dd> Include the specified file.</dl>
<dl>
<dt><code>!locale </code><i>value</i></p>
<dd> Load the following definitions only of the locale is set to <i>value</i>.</dl>
<dl>
<dt><code>!message </code><i>text</i></p>
<dd> Display <i>text</i> when the database is read unless the quiet option &#8216;(&#8216;-q is enabled.</dl>
<dl>
<dt><code>!set </code><i>variable</i> <i>value</i></p>
<dd> Sets the environment variable, <i>variable</i>, to the specified value <i>only if</i> it is not already set.</dl>
<dl>
<dt><code>!unitlist </code><i>alias</i> <i>definition</i></p>
<dd> Define a unit list alias.</dl>
<dl>
<dt><code>!utf8</code></p>
<dd> Load the following definitions only if &#8216;units&#8217; is running with UTF-8 enabled.</dl>
<dl>
<dt><code>!var </code><i>variable</i> <i>value-list</i></p>
<dd> Load the following definitions only if the environment variable, <i>variable</i> is set to one of the values listed on the space separated value list. If <i>variable</i> is not set then &#8216;units&#8217; prints an error message and ignores the following definitions.</dl>
<dl>
<dt><code>!varnot </code><i>variable</i> <i>value-list</i></p>
<dd> Load the following definitions only if the environment variable, <i>variable</i> is <i>not</i> set to one of the values listed on the space separated value list. If <i>variable</i> is not set then &#8216;units&#8217; prints an error message and ignores the following definitions.</dl>
<h2>GNU FREE DOCUMENTATION LICENSE</h2>
<h2>FILES</h2>
<p> /usr/share/units/definitions.units &#8212; the standard units data file</p>
<h2>AUTHO</h2>
<h2>Index</h2>
