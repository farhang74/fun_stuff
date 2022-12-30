## estimating pi using the Mandlebrot set

This script was inspired by https://www.youtube.com/watch?v=d0vY0CKYhPY

The idea is that if we set the number c to 0.25 and gradually add epsilon to it, the number of steps it takes to blow up to infinity is the digits of pi!!
The smaller epsilon is, the estimation is more accurate. 

For epsilon 1, we estamate pi as 2
For epsilon 0.01, we estamate pi as 30
For epsilon 0.0001, we estamate pi as 312
For epsilon 0.0000000001, we estamate pi as 314157
....
