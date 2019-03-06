package main

import (
	"os"
	"fmt"
	"github.com/gocelery/gocelery"
	"math/rand"
)

func main() {
	// initialize celery client
	url := fmt.Sprintf("amqp://platzi:%s@localhost/platzi",os.Getenv("RMQ_PASS"))
	cli, _ := gocelery.NewCeleryClient(
		gocelery.NewAMQPCeleryBroker(url),
		gocelery.NewAMQPCeleryBackend(url),
		1,
	)

	// Prepara los comandos
	taskName := "RegistraComandos.registra"
	comandos := [3]string{"uno","dos","tres"}
	
	i:= 0
	for i < 1 {
		_, err := cli.Delay(taskName, comandos[rand.Intn(3)])
		if err != nil {
			panic(err)
		}
	}
}
