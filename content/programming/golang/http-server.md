---
title: "Http Server"
date: 2020-05-24T00:49:01+05:30
 
weight: 999
---

{{< codecaption lang="golang" title="http server" >}}
package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", handler) // each request calls handler

	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}

// handler echoes the Path component of the requested URL.
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "URL.Path = %q\n", r.URL.Path)
}
{{< /codecaption >}}