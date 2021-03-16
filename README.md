# Comexim Bra Size Converter 

[**This calculator**](http://comeximcalc.herokuapp.com/) created by [@winsbe01](https://github.com/winsbe01) and [u/EuphoricToe1](https://www.reddit.com/user/EuphoricToe1) will suggest bra sizes to try when purchasing Comexim bras. 

It is intended to be a starting point for finding the correct size, but as with all bras, different styles and brands will fit everyone a little differently.

## Intro

This tool was built to convert your UK bra size to the two main systems used to size Comexim bras. The code that does the calculations can be found here, and the calculator itself is in the link above.

## Instructions for using the script 

**Thank you to Reddit user u/horstersen made [these great visual instructions](https://imgur.com/a/dqyuuOR) for using this script!**

If you would like to run the script on the command line:

* Copy everything [here](https://github.com/mathandplants/comexim/blob/main/calculator.py) and paste it into your favorite plain text editor\*. 
* Change the values (`band_size`, `cup_size`, `store_name`) at the top to your UK bra size and the store you plan on buying from.
* Copy everything again
* Go to [this shell](https://www.python.org/shell/) on python's official website, paste the entire code block into the black box, and hit enter. (If you are on mobile, you will need to switch to desktop mode.)

The final line of the output will be your size!

<sub>\*If you use and word processor like MS Word or Google Docs, please paste by right clicking + "Paste without formatting" or `ctrl + shift + V` (`cmd + shift + V` on Mac). Otherwise you will get a `NameError`. You will also want to ensure that the apostrophes (') don't get auto-formatted into slanted apostrophes (’).</sub>

## Resources

For Comexim's size chart in English, [click here.](https://www.comexim.pl/en/content/6-sprawdz-rozmiar) The original Polish size chart can be found [here.](https://www.comexim.pl/pl/content/6-sprawdz-rozmiar)

[Breakout Bras](https://www.breakoutbras.com/collections/underwire/comexim) also sells Comexim bras. Their size guide will be at the bottom of the page for every bra. They suggest using the same band size and going up 1-2 cup sizes from your normal UK size.

## Method

Like all calculators, this is just a starting point. There is no problem with taking your UK size and adding two cup sizes; I've just found that this method works better for me.

When you look at traditional UK/US sizes, one additional cup size typically adds 1 inch the difference between overbust and underbust. With Comexim, the each step in cup size is 2 centimeters, and 1 in = 2.54 cm. This means that cups change at a different rate. You can see how as cup sizes get bigger, there is a larger difference between the measurement systems and a greater need to size up, while those under a D cup may overestimate using the +2 method.

![Comparison](https://github.com/mathandplants/comexim/blob/project-info/comexim_cup_difference_cm.jpg)

The math going on behind the scenes is based on this idea. The steps for doing this are:

* Take your cup size and translate that to a numerical value - A = 1, B = 2, C = 3, etc.
* Convert this value from inches to centimeters by multiplying by 2.54
* Divide the result by 2
* This new number is the new number of cup sizes
* Determine where you are purchasing from 
* Reference a table (below) to convert that number to a letter in either UK or Comexim cup size
* Convert your band size to a EU size, as needed

## Custom Orders

Some sizes are not available by default, but Comexim is good about taking custom requests. You will need to reach out to them directly. Specifically, they do not offer bands under UK28 (EU60) or over UK40 (EU90). Some cup sizes also must be custom ordered. The calculator should have a note about this if it applies to you.

## Conversion Charts

### Band
<table>
<thead>
<tr>
<th>UK Band Size</th>
<th>Polish Band Size</th>
</tr>
</thead>
 <tbody>
  <tr> 
  <td>24</td>
  <td>50</td>
  </tr>
  
  <tr>
  <td>26</td>
  <td>55</td>
  </tr>
  
  <tr>
  <td>28</td>
  <td>60</td>
  </tr>
  
  <tr>
  <td>30</td>
  <td>65</td>
  </tr>
  
  <tr>
  <td>32</td>
  <td>70</td>
  </tr>
  
  <tr>
  <td>34</td>
  <td>75</td>
  </tr>
  
  <tr>
  <td>36</td>
  <td>80</td>
  </tr>
  
  <tr>
  <td>38</td>
  <td>85</td>
  </tr>
  
  <tr>
  <td>40</td>
  <td>90</td>
  </tr>
  
  <tr>
  <td>42</td>
  <td>95</td>
  </tr>
  
  <tr>
  <td>44</td>
  <td>100</td>
  </tr>
  
  <tr>
  <td>46</td>
  <td>105</td>
  </tr>
  
  <tr>
  <td>48</td>
  <td>110</td>
  </tr>
  
  <tr>
  <td>50</td>
  <td>115</td>
  </tr>
  
</tbody>
</table>

### Direct Cup Conversion: UK - Comexim

**Note:** This is not the same as the calculator, and these cups will have different volumes. These are just the steps between cups.

<table>
<thead>
<tr>
<th>UK Cup Size</th>
<th>Comexim Cup Size</th>
<th>Cup #</th>
</tr>
</thead>
 <tbody>
  <tr> 
  <td>A</td>
  <td>A</td>
  <td>1</td>
  </tr>
  
  <tr>
  <td>B</td>
  <td>B</td>
  <td>2</td>
  </tr>
  
  <tr>
  <td>C</td>
  <td>C</td>
  <td>3</td>
  </tr>
  
  <tr>
  <td>D</td>
  <td>D</td>
  <td>4</td>
  </tr>
  
  <tr>
  <td>DD</td>
  <td>E</td>
  <td>5</td>
  </tr>
  
  <tr>
  <td>E</td>
  <td>F</td>
  <td>6</td>
  </tr>
  
  <tr>
  <td>F</td>
  <td>G</td>
  <td>7</td>
  </tr>
  
  <tr>
  <td>FF</td>
  <td>H</td>
  <td>8</td>
  </tr>
  
  <tr>
  <td>G</td>
  <td>HH</td>
  <td>9</td>
  </tr>
  
  <tr>
  <td>GG</td>
  <td>J</td>
  <td>10</td>
  </tr>
  
  <tr>
  <td>H</td>
  <td>K</td>
  <td>11</td>
  </tr>
  
  <tr>
  <td>HH</td>
  <td>L</td>
  <td>12</td>
  </tr>
  
  <tr>
  <td>J</td>
  <td>M</td>
  <td>13</td>
  </tr>
  
  <tr>
  <td>JJ</td>
  <td>N</td>
  <td>14</td>
  </tr>
  
  <tr>
  <td>K</td>
  <td>O</td>
  <td>15</td>
  </tr>
  
  <tr>
  <td>KK</td>
  <td>P</td>
  <td>16</td>
  </tr>
  
  <tr>
  <td>L</td>
  <td>Q</td>
  <td>17</td>
  </tr>
  
  <tr>
  <td>LL</td>
  <td>R</td>
  <td>18</td>
  </tr>
  
  <tr>
  <td>M</td>
  <td>S</td>
  <td>19</td>
  </tr>
  
  <tr>
  <td>MM</td>
  <td>T</td>
  <td>20</td>
  </tr>
  
</tbody>
</table>
