# Python Turtle Mandala Patterns

Mandala is one of the most popular types of patterns to color in the trend of coloring as a form of relaxation. Mandalas are geometric patterns that are usually circular in shape. Drawing and coloring a mandala is a form of meditation for some people. They relax, their mind becomes quiet, and they may enter into a spiritual space as they concentrate on coloring in the patterns of the form.

As one of our midterm requirements in our Computer Graphics and Visual Computing Subject, we are tasked to make a mandala pattern through coding, utilizing python's turtle library. I have made three patterns and each of them has a unique design. They are:

* [Flower Power](#flower-power)
* [Dream Catcher](#dream-catcher)
* [Star Explosion](#star-explosion)

See also:
* [References](#references)
* [How I Implemented the Patterns](#how-i-implemented-the-patterns)

<br />

## Flower Power
This pattern particularly represents a flower. The term "flower power" has come to be associated with the 1960s. This slogan was used to describe the passive, peaceful resistance movement that arose in response to the [Vietnam War](https://www.history.com/topics/vietnam-war/vietnam-war-history). The flower became known as a symbol of non-violence and harmony. And as a tribute, I made a unique pattern just for that.

### Output:
<img src="https://user-images.githubusercontent.com/79429518/164236190-51f44c0c-de45-4aaf-bbba-f17d1ec54712.png" width="100%">

<br />

## Dream Catcher
Dream catchers are made to protect sleepers, especially children, from bad dreams, nightmares, and evil spirits. The meanings of each part of the dream catcher were linked to the physical world. One notable meaning is that the round shape of the dream catcher represents the earth's spherical character. During the night, the web absorbs bad dreams and releases them during the day. There are various designs on the dream catcher's web inside the circle and decided to implement a unique pattern based on the commonly used ones.

### Output:
<img src="https://user-images.githubusercontent.com/79429518/164239250-da54ad9d-4caf-47fc-842e-04721918e010.png" width="100%">

<br />

## Star Explosion
When a star reaches the end of its life, it explodes in a brilliant burst of light known as a supernova. It is beautiful and terrifying at the same time and that's why I decided to implement it. I implemented a pattern where a red supergiant is on a brink of an explosion. The patterned sphere represents a red supergiant and the petal-like pattern inside it represents the amount of light and energy it's about to release as it's about to explode.

### Output:
<img src="https://user-images.githubusercontent.com/79429518/164239630-05b8bf3d-4dd3-450d-b02a-2013aca1c3db.png" width="100%">

<br />

## References

- https://www.codeproject.com/Articles/1274883/Flower-Matrix-Composition-in-Python

- https://cwyalpha.wordpress.com/2012/08/25/thought-this-was-cool-python-turtle/

- https://cppsecrets.com/users/5440112114971061011151044611511410511897115116971189795991154956641031089746979946105110/Python-turtle-introduction.php


<br />

## How I Implemented the Patterns
I used the resources from all the links in the [references](#references) to implement all these pattern designs. I've changed a lot of code from the sources and restructured it to fit my needs. There are parts of the code where I have to reuse them in other patterns that I've implemented. For example, from the petal-like pattern from [Flower Power](#flower-power), I've reused some parts and changed some parameters like the amount of iteration that the petal is going to be drawn, and its radius and size for my [Dream Catcher](#dream-catcher). For the sphere-like pattern from [Star Explosion](#star-explosion), I've also reused some parts from [Flower Power](#flower-power) and changed the number of circles that it's going to be drawn and their radius. There are times when I have to trial and error, especially when setting the position for the next layer pattern. The rest of it is just my imagination. Although some patterns could be improved, but I'm already satisfied with the results.
