# monty_hall

Anyone who has read a book about statistics and probability must have come across the famous ‘Monty Hall’ problem. This problem was actually a part of the TV show, Lets Make a Deal . The show had two hosts: Stefan Hatos and Monty Hall after whom the problem was named.
Here how the problem goes:

"Suppose you’re on a game show, and you’re given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say №1, and the host, who knows what’s behind the doors, opens another door, say №3, which has a goat. He then says to you, “Do you want to pick door №2?” Is it to your advantage to switch your choice?"

There a number of different solutions suggested for this problem online. Most of them have heuristic explanations. Those explanations generally make perfects sense until you stumble upon a different and more confusing version of the problem. Therefore, in this blog, I wanted to share an analytical solution where the random variables are clearly defined and the probabilities are calculated. Also, I share the code for the simulation for those who are interested (click here).
First, we define three random variables:

S_i = The door we select. The probability of selecting the ith door is 1/3.

C_i = The door that has the car behind it. The probability that the car is behind the ith door is 1/3.

H_i = The door that the host opens. This is depended on S_i and C_i

The question says that we selected the door 1 and the host opened the door 3. We have two options: sticking to the door 1 or switching the door 2. We need to compute two probabilities:

1-) P(S_1 and C_1 | H_3): The probability that we selected the door 1 and door 1 has the goat behind it given the host opened the door 3.

2-) P(S_1 and C_2 | H_3): The probability that we selected the door 1 and door 2 has the goat behind it given the host opened the door 3.

If option 2 is greater than 1, then we should switch to door 2. Otherwise, we should stick to the door 1.

It is important to observe that P(S_1 and C_1 | H_3) + P(S_1 and C_2 | H_3) = 1. Because the probability of all the other events are zero. For example, P(S_1 and C_3 | H_3); given the host opened the door 3, the car can not be behind the door 3.

We need to compute two probabilities. It does not matter which one to compute because they sum to 1 as explained above. So, lets start computing option 2.
Applying the Bayes rule twice:

P(S_1 and C_2 | H_3) = P( H_3 | S_1 and C_2 ) x P(S_1 and C_2) \ P( H_3)

Lets look at the terms one by one:

P( H_3 | S_1 and C_2 ) equals to 1 because given that we selected door 1 and the car is behind the door 2, the host has to open the door 3.

P(S_1 and C_2) equals (1/3)² = 1/9 because these two are independent events i.e., the selection of one of the doors does not affect where the car is.

P( H_3) = P( H_3 | S_1 and C_2 ) x P(S_1 and C_2) + P( H_3 | S_1 and C_2) x P(S_1 and C_1) because of the law of total probability.

P( H_3 | S_1 and C_1 ) equals to 1/2 because the host has two options to open.

P(S_1 and C_1) = 1/9 because these two are independent events i.e., the selection of one of the doors does not affect where the car is.

Putting everything together:

P(S_1 and C_2 | H_3) = (1/9 x 1) / ((1/9 x 1) + (1/9 x 1/2)) = 2 /3

P(S_1 and C_1 | H_3) = 1– 2/3 = 1/3

So, it makes sense to switch to door 2 because P(S_1 and C_2 | H_3) > P(S_1 and C_1 | H_3).

Now, lets make the question a little more complicating and have 10 doors. We select door 1, then the host opens 8 doors (doors 2,3,4,5,6,7,8,9) leaving one door closed (door 10). Then, he asks if want to switch or not. I will show that the framework presented above can also be followed to solve this problem. We have two probability to compute:

1-) P(S_1 and C_1 | H_2,H_3,H_4,H_5,H_6,H_7,H_8,H_9): The probability that we selected the door 1 and door 1 has the goat behind it given the host opened the door 2,3,4,5,6,7,8,9.

2-) P(S_1 and C_10 | H_2,H_3,H_4,H_5,H_6,H_7,H_8,H_9): The probability that we selected the door 1 and door 10 has the goat behind it given the host opened the doors 2,3,4,5,6,7,8,9.
P(S_1 and C_1 | H_2,H_3,H_4,H_5,H_6,H_7,H_8,H_9) = P(H_2,H_3,H_4,H_5,H_6,H_7,H_8,H_9 | S_1 and C_1)P(S_1 and C_1) / P(H_2,H_3,H_4,H_5,H_6,H_7,H_8,H_9) = (1/9 * 1/100) / ((1/9 * 1/100) + (1* 1/100)) = 1/10

P(S_1 and C_10 | H_2,H_3,H_4,H_5,H_6,H_7,H_8,H_9) = 1–1/10 = 9/10

Therefore, we should swictch the door 10. I am also sharing the simulation that validates the results (click here). Enjoy!

