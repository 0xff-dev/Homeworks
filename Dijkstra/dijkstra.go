package main

import "fmt"

var maxLength int = 9999999

func generate(row, col int) ([6][6]int, []int) {
	res := [6][6]int{
		{0, 1, 12, maxLength, maxLength, maxLength},
		{maxLength, 0, 9, 3, maxLength, maxLength},
		{maxLength, maxLength, 0, maxLength, 5, maxLength},
		{maxLength, maxLength, 4, 0, 13, 15},
		{maxLength, maxLength, maxLength, maxLength, 0, 4},
		{maxLength, maxLength, maxLength, maxLength, maxLength, 0},
	}
	dis := make([]int, row)
	for i := 0; i < row; i++ {
		dis[i] = res[0][i]
	}
	return res, dis
}

func solve() {
	disMap, dis := generate(6, 6)
	// 启动算法
	visited := make([]bool, 6)
	visited[0] = true
	for i := 0; i < 5; i++ {
		minDistance := maxLength
		minIndex := -1
		for j := 0; j < 6; j++ {
			if !visited[j] && dis[j] < minDistance {
				minDistance = dis[j]
				minIndex = j
			}
		}
		visited[minIndex] = true
		for j := 0; j < 6; j++ {
			if !visited[j] && disMap[minIndex][j]+minDistance < dis[j] {
				dis[j] = disMap[minIndex][j] + minDistance
			}
		}
	}
	fmt.Println(dis)
}

func main() {
	solve()
}
