# 🎯 **Pendulum Simulator** 🌊

Simule um pêndulo simples de forma interativa e visualize seu movimento oscilatório baseado em cálculos físicos realistas. 🚀

---

## 📊 **Sobre o Projeto**

O **Pendulum Simulator** é uma aplicação em Python desenvolvida com **Pygame**, focada em simular o comportamento de um pêndulo simples usando uma abordagem modular.

📌 **Versão Inicial:**  
- 🎭 Apenas um único pêndulo.  
- ⚙️ Física baseada nas equações do movimento.  
- 🎨 Renderização visual básica usando Pygame.  
- ⏳ Animação em tempo real.  

🚧 **O que ainda não tem:**  
- ❌ Sliders para ajuste de parâmetros.  
- ❌ Adição de múltiplos pêndulos.  
- ❌ Interface gráfica avançada.  

---

## ⚡ **Física do Pêndulo Simples**

O movimento do pêndulo é governado por uma equação diferencial não linear derivada das leis de Newton.

### 📐 **Equação do Movimento**

```
α = -(g / L) * sin(θ)
```

Onde:
- **α (alpha)** = Aceleração angular (rad/s²)
- **g** = Gravidade (definida como 9.81 m/s² ou ajustável)
- **L** = Comprimento da haste do pêndulo (em metros)
- **θ (theta)** = Ângulo de oscilação em radianos

Essa equação mostra que a aceleração angular do pêndulo é proporcional ao seno do seu ângulo em relação à vertical e inversamente proporcional ao comprimento da haste.

---

### 🔄 **Cálculo da Atualização do Estado**

O simulador resolve numericamente essa equação usando o **método de Euler**, atualizando a cada frame:

1. **Cálculo da aceleração angular:**
   ```
   α = -(g / L) * sin(θ)
   ```

2. **Atualização da velocidade angular:**
   ```
   ω = ω + α * Δt
   ```

3. **Atualização do ângulo:**
   ```
   θ = θ + ω * Δt
   ```

4. **Conversão para coordenadas (x, y):**
   ```
   x = x₀ + L * sin(θ)
   y = y₀ + L * cos(θ)
   ```

---

## 🚀 **Como Rodar o Projeto**

### 📦 **Pré-requisitos**

- **Python 3.10+**
- **Poetry** (para gerenciamento de dependências)

### ⚙️ **Instalação**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/JVitoroliv3ira/pendulum-simulator
   cd pendulum-simulator
   ```

2. **Instale as dependências com Poetry:**

   ```bash
   poetry install
   ```

3. **Ative o ambiente virtual:**

   ```bash
   poetry shell
   ```

4. **Execute o simulador:**

   ```bash
   python src/main.py
   ```

---

## 🎨 **Funcionalidades**

- 🟢 **Simulação de um pêndulo oscilando livremente** com base nas equações do movimento.  
- 🟢 **Visualização com Pygame** e atualização em tempo real.  
- 🟢 **Parâmetros físicos configuráveis** no código (`config.py`).  

---

## 🔧 **Estrutura do Projeto**

```
pendulum_simulator/
├── main.py                  # Ponto de entrada da aplicação
├── simulation/
│   └── pendulum.py          # Lógica física do pêndulo
├── visualization/
│   ├── render.py            # Código de renderização com Pygame
│   └── config.py            # Configurações gerais (cores, dimensões)
```

---

## 🛠️ **Possíveis Melhorias Futuras**

- 🎛️ **Sliders para ajuste de parâmetros em tempo real**  
- 🔗 **Múltiplos Pêndulos**  
- ⚡ **Simulação de pêndulos acoplados**  
- 📊 **Gráficos de energia (cinética/potencial)**  
- 🌍 **Simulação com resistência do ar**  

---

## 👨‍💻 **Contribuindo**

1. **Fork o repositório**  
2. Crie uma nova branch:  
   ```bash
   git checkout -b feature-nova
   ```  
3. Faça suas alterações e envie um **Pull Request**!  

---

## 🧠 **Créditos**

Desenvolvido por João Vitor de Oliveira Santos 🚀  
Projeto baseado nas leis da física para experimentos interativos e educacionais.