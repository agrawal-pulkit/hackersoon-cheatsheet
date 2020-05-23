---
title: "Http Request"
date: 2020-05-24T00:43:25+05:30
 
weight: 999
---

{{< codecaption lang="golang" title="http request" >}}
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

func main() {
	fmt.Println(os.Args[1:])

	for _, url := range os.Args[1:] {
		if strings.HasPrefix(url, "http://") {
			fmt.Println(url)
		}
		res, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch:%v\n", err)
			os.Exit(1)
		}
		fmt.Printf("%v", res.Status)
		b, err := ioutil.ReadAll(res.Body)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: redaing %s: %v\n ", url, err)
			os.Exit(1)
		}
		fmt.Printf("%s ", b)
	}
}
{{< /codecaption >}}