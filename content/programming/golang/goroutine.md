---
title: "Goroutine"
date: 2019-12-15T02:17:40+05:30
 
weight: 999
---


This is useful for understand golang goroutines.
{{< codecaption lang="golang" title="goroutine & channel" >}}
package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

func main() {
	fmt.Println("fetch all url: this example is used to demonstarte how concurrency works in golang")

	start := time.Now()
	ch := make(chan string)

	for _, url := range os.Args[1:] {
		go fetch(url, ch) // start a gorotuine
	}

	for range os.Args[1:] {
		fmt.Println(<-ch) //recieve from channel
	}

	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}

func fetch(url string, ch chan<- string) {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err)
		return
	}

	nbytes, err := io.Copy(ioutil.Discard, resp.Body)
	resp.Body.Close() // don't leak resources
	if err != nil {
		ch <- fmt.Sprintf("while reading %s: %v", url, err)
		return
	}

	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.2fs  %7d  %s", secs, nbytes, url)

}
{{< /codecaption >}}