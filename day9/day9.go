package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println("day9")
	score := map[int]int{}

	play(score, 9, 25)
	printScores(score)
	score = map[int]int{}

	play(score, 10, 1618)
	printScores(score)

	score = map[int]int{}
	play(score, 13, 7999)
	printScores(score)

	score = map[int]int{}
	play(score, 17, 1104)
	printScores(score)

	score = map[int]int{}
	play(score, 21, 6111)
	printScores(score)

	score = map[int]int{}
	play(score, 30, 5807)
	printScores(score)

	score = map[int]int{}
	play(score, 470, 72170)
	printScores(score)

	score = map[int]int{}
	play(score, 470, 7217000)
	printScores(score)
}

func printScores(score map[int]int) {
	scores := []int{}
	for _, v := range score {
		scores = append(scores, v)
	}

	sort.Ints(scores)
	fmt.Println(scores)

}

type Node struct {
	Val  int
	Next *Node
	Prev *Node
}

func play(score map[int]int, players int, high int) {
	head := &Node{Val: 0}
	head.Next = head
	head.Prev = head
	curr := head
	for i := 1; i <= high; i++ {
		if i%23 == 0 {
			for i := 0; i < 7; i++ {
				curr = curr.Prev
			}
			val := curr.Val
			//delink curr node
			curr.Prev.Next = curr.Next
			curr.Next.Prev = curr.Prev
			//set curr
			curr = curr.Next
			//fmt.Printf("%v -> %v -> %v", curr.Prev.Val, curr.Val, curr.Next.Val)
			score[i%players] = score[i%players] + val + i
			continue
		}
		newNode := &Node{Val: i}
		newNode.Next = curr.Next.Next
		newNode.Prev = curr.Next

		curr.Next.Next = newNode
		newNode.Next.Prev = newNode
		curr = newNode
	}
}
