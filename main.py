from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens. Para maior segurança, substitua por ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["GET"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

# Dados fictícios de acomodações com múltiplas imagens
acomodacoes = [
    {
        "id": 1,
        "nome": "Pousada Azul",
        "cidade": "Florianópolis",
        "preco": 200,
        "images": [
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/f4/d0/5e/pousada-azul.jpg?w=1200&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/f4/cc/ef/pousada-azul.jpg?w=1200&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/f4/cd/5a/pousada-azul.jpg?w=1200&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-s/01/73/ec/4b/florianopolis.jpg?w=600&h=-1&s=1"
        ]
    },
    {
        "id": 2,
        "nome": "Porto Sol",
        "cidade": "São Paulo",
        "preco": 350,
        "images": [
            "https://img.freepik.com/fotos-gratis/representacao-elegante-do-design-interior_23-2151892468.jpg",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/8c/3d/88/hotel-porto-sol-beach.jpg?w=1400&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/8c/3d/32/hotel-porto-sol-beach.jpg?w=1400&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/8c/3d/01/hotel-porto-sol-beach.jpg?w=1400&h=-1&s=1"
        ]
    },
    {
        "id": 3,
        "nome": "Resort Paraíso",
        "cidade": "Florianópolis",
        "preco": 500,
        "images": [
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/c3/a5/df/piscina-aquecida.jpg?w=500&h=400&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/af/ae/dd/jurere-beach-village.jpg?w=1400&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/af/b4/65/jurere-beach-village.jpg?w=1400&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/af/b0/d9/jurere-beach-village.jpg?w=1400&h=-1&s=1"
        ]
    },
    {
        "id": 4,
        "nome": "Hostel Aventura",
        "cidade": "Rio de Janeiro",
        "preco": 100,
        "images": [
            "https://www.hostelworld.com/blog/wp-content/uploads/2019/02/Bonita-Ipanema.jpg",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/24/f3/1c/1b/vista-apartamento-luxo.jpg?w=700&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/24/f3/1c/18/lk-design-hotel.jpg?w=700&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/6a/8e/9b/wk-design-hotel.jpg?w=1400&h=-1&s=1"
        ]
    },
    {
        "id": 5,
        "nome": "Pousada Mar Azul",
        "cidade": "Florianópolis",
        "preco": 200,
        "images": [
            "https://pousada-azul-floripa.hotelflorianopolis.com/data/Images/OriginalPhoto/1749/174958/174958899/image-florianopolis-pousada-azul-floripa-5.JPEG",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/c3/a5/df/piscina-aquecida.jpg?w=500&h=400&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/87/b1/99/mar-de-canasvieiras-hotel.jpg?w=2000&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/9f/f4/52/mar-de-canasvieiras-hotel.jpg?w=2000&h=-1&s=1"
        ]
    },
    {
        "id": 6,
        "nome": "Hotel Sunrise",
        "cidade": "São Paulo",
        "preco": 350,
        "images": [
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/9f/f4/59/mar-de-canasvieiras-hotel.jpg?w=2000&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/f2/af/e8/apartamento-standard.jpg?w=1200&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/f2/ae/6f/apartamento-standard.jpg?w=2400&h=-1&s=1" ,
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/87/b1/7c/mar-de-canasvieiras-hotel.jpg?w=2000&h=-1&s=1"
       ]
    },
    {
        "id": 7,
        "nome": "Pedra Encantada",
        "cidade": "Florianópolis",
        "preco": 500,
        "images": [
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/88/57/ea/slaviero-baia-norte-florianopo.jpg?w=1100&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/87/b1/99/mar-de-canasvieiras-hotel.jpg?w=2000&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/88/57/e3/slaviero-baia-norte-florianopo.jpg?w=500&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/88/57/be/slaviero-baia-norte-florianopo.jpg?w=500&h=-1&s=1"
        ]
    },
    {
        "id": 8,
        "nome": "Hostel Vila Rica",
        "cidade": "Rio de Janeiro",
        "preco": 100,
        "images": [
            "https://www.hostelworld.com/blog/wp-content/uploads/2019/02/Bonita-Ipanema.jpg",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/88/57/b3/slaviero-baia-norte-florianopo.jpg?w=1100&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/88/57/e3/slaviero-baia-norte-florianopo.jpg?w=500&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/3a/46/22/luxury-room-double--v10316418.jpg?w=2400&h=-1&s=1"
        ]
    }
]

@app.get("/acomodacoes", response_model=List[dict])
def listar_acomodacoes(cidade: Optional[str] = Query(None, description="Filtrar por cidade")):
    if cidade:
        resultado = [a for a in acomodacoes if a["cidade"].lower() == cidade.lower()]
        if resultado:
            return resultado
        raise HTTPException(status_code=404, detail="Nenhuma acomodação encontrada nesta cidade.")
    return acomodacoes

@app.get("/acomodacoes/{id}", response_model=dict)
def obter_acomodacao(id: int):
    for acomodacao in acomodacoes:
        if acomodacao["id"] == id:
            return acomodacao
    raise HTTPException(status_code=404, detail="Acomodação não encontrada.")
