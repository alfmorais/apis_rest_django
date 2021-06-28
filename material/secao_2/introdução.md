# Introdução às APIs REST

Muitas APIS encontradas na Internet utilizam um conceito chamado REST, que significa <b>Representational State Transfer</b>, ou Transferência Representacional de Estado.

Entender o que é <b>REST</b> irá ajudar a você a desenvolver melhores <b>APIs</b> para os sistemas que desenvolve. 

Você já deve ter ouvido falar também em <b>RESTfull</b>, que é um padrão de criação de APIs amplamente utilizado, e muitas pessoas até mesmo confudem achando que <b>REST</b> é diferente de <b>RESTfull</b>. 

No final das contas, estamos falando da criação de uma interface de comunicação utilizando puramente *HTTP*. 

## APIs = Application Programming Interface 

Uma API nada mais é do que uma interface de comunicação de aplicação de forma programática. Ou seja, criamos uma interface para que diferentes aplicações se comuniquem de forma simples e eficiente. Criamos estas interfaces, chamadas APIs utilizando padrões de design chamado *RESTfull*. Estas APIs são chamadas *APIs REST*. 

## REST - Representational State Transfer

O protocolo *HTTP*, que é onde a internet "roda" é por design, sem estado. 

Isso significa que toda requisição feita a um servidor é única pois estas requisições não guardam dados (Estados) entre uma requisição e outra.

É como se toda vez que você encontrasse um amigo tivesse que se apresentar para ele novamente. Pois nem você e nem seu amigo guardam dados (estados) entre vocês.

O *REST* não muda isso, mais coloca toda a responsabilidade de "lembrar" os dados (estados) da requisição no cliente, que pode ser seu navegador / computador / aplicação. 

Isso porque a cada requisição, o servidor que responde pela mesma pode ser diferente. Ele pode nunca ter tido contado com o cliente que o está contactando. Por outro lado, o cliente é o mesmo e o cliente sabe quais dados precisa seja para realizar autenticações ou mesmo para acessar diferentes *endpoints*.

