package main
// Estructura de https://github.com/gocelery/gocelery

import (
	"fmt"
	"time"
	"github.com/gocelery/gocelery"
)

// Celery Task
var comandos = make(map[string]int)
func registra(comando string) {
	fmt.Println( comando )
	comandos[comando]++
	fmt.Println( comandos )
}

func main() {
	// Crea el broker y el backend
	celeryBroker := gocelery.NewRedisCeleryBroker("redis://")
	celeryBackend := gocelery.NewRedisCeleryBackend("redis://")

	// Usa dos workers
	celeryClient, _ := gocelery.NewCeleryClient(celeryBroker, celeryBackend, 1)

	// Registra la función
	celeryClient.Register("tasks.registra", registra)

	// Arranca el worker
	fmt.Println( "Arranca el worker" )
	go celeryClient.StartWorker()

	// Espera y para 
	time.Sleep(120 * time.Second)
	celeryClient.StopWorker()
}
