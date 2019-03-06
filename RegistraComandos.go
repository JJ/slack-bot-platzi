package main
// Estructura de https://github.com/gocelery/gocelery

import (
	"os"
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
	fmt.Println(os.Getenv("RMQ_PASS"))
	url := fmt.Sprintf("amqp://platzi:%s@localhost/platzi",os.Getenv("RMQ_PASS"))
	fmt.Println(url)
	celeryBroker := gocelery.NewAMQPCeleryBroker(url)
	celeryBackend := gocelery.NewAMQPCeleryBackend(url)

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
