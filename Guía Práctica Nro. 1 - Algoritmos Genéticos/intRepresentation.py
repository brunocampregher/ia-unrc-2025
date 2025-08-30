import random

# ---------------------------
# Parámetros
# ---------------------------
POP_SIZE = 20 # Tamaño de la población
GENS = 30 # Número de generaciones
CXPB = 0.8 # Probabilidad de cruce
MUTPB = 0.05 # Probabilidad de mutación
GENOME_LENGTH = 8 # Cantidad de bits
NUM = 27 # Número decimal objetivo

# ---------------------------
# Función de fitness
# ---------------------------
def fitness(individual):
  return abs(NUM - bin_a_dec(individual))

# ---------------------------
# Crear población
# ---------------------------
def create_individual():
  return [random.randint(0, 1) for _ in range(GENOME_LENGTH)]

def create_population():
  return [create_individual() for _ in range(POP_SIZE)]

# ---------------------------
# Operadores genéticos
# ---------------------------
def selection(population):
  # Selección por torneo
  k = 3
  selected = []
  for _ in range(POP_SIZE):
    aspirants = random.sample(population, k)
    winner = min(aspirants, key=fitness)
    selected.append(winner)
  return selected

def crossover(p1, p2):
  # Combinación de un punto
  if random.random() < CXPB:
    point = random.randint(1, GENOME_LENGTH - 1)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]
  return p1[:], p2[:]

def mutate(individual):
  for i in range(GENOME_LENGTH):
    if random.random() < MUTPB:
      individual[i] = 1 - individual[i]  # Flip bit
  return individual

# Funciones auxiliares
# ---------------------------
def bin_a_dec(individual):
  valor = 0
  individuo = individual[::-1]
  for i in range(GENOME_LENGTH):
    valor += individuo[i] * (2 ** i)
  return valor

# Algoritmo principal
# ---------------------------
def genetic_algorithm():
  population = create_population()
  for gen in range(GENS):
    # Evaluar y mostrar el mejor
    population.sort(key=fitness)
    print(f"Gen {gen}: Mejor = {population[0]} Fitness = {fitness(population[0])}")
    # Selección
    selected = selection(population)
    # Reproducción
    next_gen = []
    for i in range(0, POP_SIZE, 2):
      offspring1, offspring2 = crossover(selected[i], selected[i+1])
      next_gen.append(mutate(offspring1))
      next_gen.append(mutate(offspring2))
    population = next_gen

  return min(population, key=fitness)

# ---------------------------
# Ejecutar
# ---------------------------
best = genetic_algorithm()
print(f"Mejor individuo encontrado: Binario = {best}, Decimal = {bin_a_dec(best)}, Fitness = {fitness(best)}")

