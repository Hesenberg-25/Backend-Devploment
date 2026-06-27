# 🗺️ Master Learning Roadmap

**Total Timeline:** ~36 months | **Daily commitment:** 2–3 hrs/day
**Goal:** Backend Dev + CS Core + AI/ML/RAG — fully hireable full-stack backend + AI engineer

---

## 📌 Overview

| Phase | Topic | Duration |
|-------|-------|----------|
| 1 | Python Foundations | 1 month |
| 2 | Database Mastery | 2 months |
| 3 | API Development | 2 months |
| 4 | Auth, Security & Async | 2 months |
| 5 | Quality & Containers | 2 months |
| 6 | Scaling & Infrastructure | 2 months |
| 7 | Architecture & Deployment | 2 months |
| 8 | Portfolio Finalization | 1 month |
| 9 | CS Core — Networks & OS | 3 months |
| 10 | DSA — Post Recursion (Striver) | 5 months |
| 11 | AI/ML Foundations | 4 months |
| 12 | Deep Learning | 3 months |
| 13 | RAG & LLM Engineering | 2 months |
| — | Buffer (exams, catch-up, revision) | 3 months |
| **Total** | | **~36 months** |

> ⚠️ DSA (Phase 10) runs **parallel** with Phases 9–11. 30–45 min DSA daily during those phases.

---

## Phase 1 — Python Foundations
**Duration:** 1 month

### Python Advanced
- [ ] OOP for Python
- [ ] Decorators
- [ ] Generators
- [ ] Context managers
- [ ] Type hints
- [ ] Exception handling (custom exceptions)
- [ ] File I/O and JSON handling
- [ ] Virtual environments, pip, requirements.txt
- [ ] Environment variables (.env)
- [ ] Logging

### Git & Tooling
- [ ] Branching strategy basics
- [ ] Writing clean commit history

### Projects
- [ ] Refactor existing CLI project with logging, exceptions, type hints

### ✅ Milestone
- Strong Python fundamentals beyond basics
- Clean, professional coding habits in place

---

## Phase 2 — Database Mastery
**Duration:** 2 months

### SQL Querying
- [ ] All JOIN types (INNER, LEFT, RIGHT, FULL OUTER)
- [ ] Subqueries (correlated vs non-correlated)
- [ ] GROUP BY / HAVING
- [ ] Window functions (ROW_NUMBER, RANK, PARTITION BY)
- [ ] Common Table Expressions (WITH clause)

### Schema Design & Normalization
- [ ] 1NF, 2NF, 3NF
- [ ] Denormalization tradeoffs
- [ ] Foreign keys and constraints

### Indexing & Query Optimization
- [ ] B-tree index structure
- [ ] Composite indexes
- [ ] EXPLAIN / EXPLAIN ANALYZE

### Transactions & ACID
- [ ] ACID properties in practice
- [ ] Isolation levels
- [ ] Deadlocks

### ORM (SQLAlchemy)
- [ ] Models and relationships
- [ ] ORM vs raw SQL
- [ ] Alembic migrations

### Projects
- [ ] Redesign TrueBalance schema with normalization + indexes
- [ ] Migrate TrueBalance to SQLAlchemy + Alembic

### ✅ Milestone
- Comfortable designing schemas from scratch
- Can read and optimize query plans
- ORM-based data layer working in TrueBalance

---

## Phase 3 — API Development
**Duration:** 2 months

### FastAPI Core
- [ ] Routing — path params, query params, request body
- [ ] Response models

### Pydantic & Validation
- [ ] Custom validators
- [ ] Nested models
- [ ] Field constraints

### Dependency Injection & Middleware
- [ ] Depends() pattern
- [ ] Shared DB session
- [ ] Custom middleware
- [ ] CORS configuration
- [ ] Custom exception handlers

### REST API Design Principles
- [ ] Resource naming conventions
- [ ] HTTP verb-to-action mapping
- [ ] Status code precision (200/201/204/400/401/403/404/422)
- [ ] Idempotency

### Pagination & Versioning
- [ ] Limit/offset pagination
- [ ] Cursor-based pagination
- [ ] API versioning strategies
- [ ] Rate limiting concepts

### Projects
- [ ] Rebuild TrueBalance routes with clean DI pattern
- [ ] Add pagination + correct status codes
- [ ] Generate full OpenAPI/Swagger docs

### ✅ Milestone
- Can design a clean, well-documented REST API from scratch
- TrueBalance API follows REST best practices

---

## Phase 4 — Auth, Security & Async
**Duration:** 2 months
> ⚠️ Dense phase. Reduce to 1.5 hrs/day if needed. DSA takes priority here.

### Authentication
- [ ] Password hashing (bcrypt)
- [ ] JWT structure (access/refresh tokens)
- [ ] OAuth2 password flow
- [ ] Redis for session/token storage

### Authorization
- [ ] Role-Based Access Control (RBAC)
- [ ] Endpoint-level permission checks

### Security Hardening
- [ ] OWASP Top 10 awareness
- [ ] SQL injection prevention
- [ ] Input validation as defense
- [ ] Secrets management

### Async Programming
- [ ] asyncio fundamentals (event loop, coroutines)
- [ ] async/await in FastAPI
- [ ] asyncpg for async PostgreSQL
- [ ] When async helps vs doesn't

### Projects
- [ ] Build full auth system in TrueBalance (register/login/roles)
- [ ] Run OWASP security checklist on TrueBalance
- [ ] Convert key TrueBalance endpoints to async

### ✅ Milestone
- Secure, role-protected API
- Understand async tradeoffs, not just syntax

---

## Phase 5 — Quality & Containers
**Duration:** 2 months

### Testing
- [ ] pytest fundamentals (fixtures, parametrize)
- [ ] Unit tests
- [ ] Integration tests (TestClient)
- [ ] Mocking

### Docker Fundamentals
- [ ] Images vs containers
- [ ] Dockerfile syntax
- [ ] Multi-stage builds

### Docker Compose & Multi-Container Setup
- [ ] docker-compose orchestration
- [ ] Volumes (data persistence)
- [ ] Container networking

### Projects
- [ ] Achieve 70%+ test coverage on TrueBalance
- [ ] Fully containerize TrueBalance (app + Postgres + Redis)

### ✅ Milestone
- Confident writing tests for any new feature
- TrueBalance runs anywhere via docker-compose

---

## Phase 6 — Scaling & Infrastructure
**Duration:** 2 months

### Redis & Caching
- [ ] Key-value data types
- [ ] Cache-aside pattern
- [ ] TTL and cache invalidation

### Message Queues
- [ ] Celery + Redis broker
- [ ] Background job processing

### Linux / CLI
- [ ] File permissions, process management
- [ ] SSH basics
- [ ] grep/sed/awk, bash scripting

### Git Deepening
- [ ] Branching strategy (feature/main/dev)
- [ ] Merge vs rebase
- [ ] Conflict resolution

### Projects
- [ ] Add caching layer to TrueBalance's most expensive query
- [ ] Build one Celery background job pipeline
- [ ] Write bash script for local dev setup automation

### ✅ Milestone
- Measurable performance improvement via caching
- Comfortable with Linux server environment

---

## Phase 7 — Architecture & Deployment
**Duration:** 2 months

### System Design Fundamentals
- [ ] Client-server request lifecycle
- [ ] Horizontal vs vertical scaling
- [ ] Load balancing concepts

### Deployment
- [ ] Deploy to Render/Railway
- [ ] AWS basics (EC2 or equivalent)

### CI/CD
- [ ] GitHub Actions — automated testing pipeline
- [ ] Continuous deployment on merge

### Observability
- [ ] Structured logging in production
- [ ] Basic error tracking (Sentry or equivalent)

### Projects
- [ ] Draw full TrueBalance architecture diagram
- [ ] Deploy TrueBalance live with working CI/CD

### ✅ Milestone
- Can explain system design tradeoffs out loud
- TrueBalance is live and auto-deploying

---

## Phase 8 — Portfolio Finalization
**Duration:** 1 month

### Second Project
- [ ] Build small standalone project (e.g. URL shortener with rate limiting)

### Documentation
- [ ] Polished README for TrueBalance
- [ ] Embedded architecture diagram
- [ ] Clean GitHub commit history

### Resume & Interview Prep
- [ ] Resume/LinkedIn project descriptions finalized
- [ ] Mock interview — explain TrueBalance end-to-end

### ✅ Milestone
- Portfolio recruiter-ready for backend roles
- Can defend every design decision confidently

---

## Phase 9 — CS Core: Networks & OS
**Duration:** 3 months
> 💡 Run DSA (Phase 10) parallel here — 30–45 min DSA daily

### Computer Networks (Month 1–2)
- [ ] OSI model overview
- [ ] TCP vs UDP
- [ ] HTTP/HTTPS deep dive (headers, methods, status codes)
- [ ] DNS — how it works
- [ ] IP addressing, subnets (basics)
- [ ] Sockets and connections
- [ ] TLS/SSL basics
- [ ] CDN, proxies, load balancers
- [ ] WebSockets vs HTTP polling

### Operating Systems (Month 2–3)
- [ ] Processes vs threads
- [ ] Context switching
- [ ] Concurrency — race conditions, mutex, semaphores
- [ ] Deadlocks (detection + prevention)
- [ ] Memory management basics (stack vs heap, virtual memory)
- [ ] File system basics
- [ ] I/O basics

> ❌ Skip: OS scheduling algorithms (FCFS, SJF), hardware layers, formal proofs — not needed for backend

### Resources
- Networks: *Computer Networking: A Top-Down Approach* (Kurose) — Ch 1–4 enough
- OS: *Operating Systems: Three Easy Pieces* (free online) — selective chapters
- Practice: InterviewBit / GFG CN + OS question banks

### ✅ Milestone
- Can answer CN + OS interview questions confidently
- Understand how HTTP, TCP, and processes work under the hood

---

## Phase 10 — DSA: Post-Recursion (Striver Sheet)
**Duration:** 5 months (parallel with Phases 9–12)
> 💡 30–45 min daily alongside main phase. Full focus on weekends.

### Topics (Striver SDE Sheet order)
- [ ] Arrays (hard problems)
- [ ] Binary Search
- [ ] Linked Lists
- [ ] Stacks & Queues
- [ ] Trees (Binary Tree, BST)
- [ ] Heaps / Priority Queue
- [ ] Greedy
- [ ] Dynamic Programming
- [ ] Graphs (BFS, DFS, Dijkstra, Topo Sort)
- [ ] Tries
- [ ] Bit Manipulation

### Revision Strategy
- Solve problem → note pattern → revisit in 1 week → revisit in 1 month
- Use Notion or Anki for pattern tracking

### ✅ Milestone
- Can solve medium Leetcode problems independently
- Recognizes patterns, not just solutions
- Ready for DSA interview rounds

---

## Phase 11 — AI/ML Foundations
**Duration:** 4 months

### Math Refresh (Month 1 — parallel with coding)
- [ ] Linear algebra (vectors, matrices, dot product)
- [ ] Probability & statistics (distributions, Bayes)
- [ ] Calculus (derivatives, chain rule — intuition only)
- [ ] Gradient descent intuition

### Core ML (Month 1–3)
- [ ] Supervised vs unsupervised vs reinforcement learning
- [ ] Linear regression, logistic regression
- [ ] Decision trees, random forests
- [ ] SVM (intuition)
- [ ] K-means clustering
- [ ] Model evaluation (accuracy, precision, recall, F1, AUC)
- [ ] Overfitting, underfitting, regularization
- [ ] Train/val/test split, cross-validation
- [ ] Feature engineering basics

### Tools & Practice (Month 3–4)
- [ ] NumPy, Pandas
- [ ] Scikit-learn
- [ ] Matplotlib / Seaborn
- [ ] Jupyter Notebooks
- [ ] Build 2–3 end-to-end ML projects (Kaggle datasets)

### Resources
- *Hands-On Machine Learning* — Aurélien Géron
- fast.ai (practical, top-down)
- Andrew Ng's ML Specialization (Coursera)

### ✅ Milestone
- Can build, train, evaluate ML models from scratch
- Understand bias-variance tradeoff, overfitting, regularization
- 2–3 ML projects on GitHub

---

## Phase 12 — Deep Learning
**Duration:** 3 months

### Neural Networks Fundamentals
- [ ] Perceptron, activation functions
- [ ] Forward pass, backpropagation
- [ ] Loss functions (MSE, cross-entropy)
- [ ] Optimizers (SGD, Adam)
- [ ] Batch normalization, dropout

### CNNs (Computer Vision basics)
- [ ] Convolution, pooling
- [ ] ResNet, VGG architectures (conceptual)

### RNNs & Sequence Models
- [ ] RNN, LSTM, GRU intuition
- [ ] Vanishing gradient problem

### Transformers & Attention
- [ ] Attention mechanism
- [ ] Self-attention
- [ ] Transformer architecture
- [ ] BERT, GPT intuition

### Tools
- [ ] PyTorch (preferred) or TensorFlow
- [ ] HuggingFace Transformers library
- [ ] Fine-tune a small pre-trained model

### Resources
- fast.ai Part 1 & 2
- *Deep Learning* — Ian Goodfellow (reference)
- Andrej Karpathy — *Neural Networks: Zero to Hero* (YouTube)

### ✅ Milestone
- Understand transformer architecture deeply
- Can fine-tune HuggingFace models
- At least 1 DL project deployed

---

## Phase 13 — RAG & LLM Engineering
**Duration:** 2 months

### LLM Fundamentals
- [ ] How LLMs work (tokens, context window, temperature)
- [ ] Prompt engineering (zero-shot, few-shot, CoT)
- [ ] LLM APIs (OpenAI, Anthropic, Gemini)

### RAG (Retrieval-Augmented Generation)
- [ ] Embeddings and vector search
- [ ] Vector databases (Pinecone, Chroma, Weaviate)
- [ ] Chunking strategies
- [ ] Retrieval pipeline design
- [ ] Reranking
- [ ] Evaluation of RAG systems

### Frameworks
- [ ] LangChain / LlamaIndex (one of them)
- [ ] LangSmith or equivalent for tracing

### Production RAG
- [ ] FastAPI + RAG pipeline integration (your backend skills apply here)
- [ ] Streaming responses
- [ ] Cost optimization (token management)

### Projects
- [ ] Build a RAG app (e.g. chat with your own docs / codebase)
- [ ] Deploy it via your existing CI/CD pipeline

### ✅ Milestone
- Can design and deploy a production RAG system
- Backend + AI skills merge — full-stack AI backend engineer profile

---

## 🧠 Skills Checklist

### Backend
- [ ] Advanced Python + Async
- [ ] Advanced SQL + Schema design
- [ ] SQLAlchemy + Alembic
- [ ] FastAPI + REST design
- [ ] JWT/OAuth2 Auth + RBAC
- [ ] pytest + Docker + CI/CD
- [ ] Redis, Celery, message queues
- [ ] System design basics
- [ ] Cloud deployment (AWS/Render)
- [ ] Observability (structured logs, Sentry)

### CS Core
- [ ] Computer Networks (HTTP, TCP, DNS, TLS)
- [ ] OS (processes, threads, concurrency, memory)
- [ ] DBMS theory (already in Phase 2)

### DSA
- [ ] All major data structures
- [ ] Core algorithms (sorting, graphs, DP)
- [ ] Leetcode medium — consistent solve rate

### AI/ML
- [ ] ML fundamentals + Scikit-learn
- [ ] Deep Learning + PyTorch
- [ ] Transformers + HuggingFace
- [ ] RAG pipelines + vector DBs
- [ ] LLM API integration

---

## 🎯 Portfolio Targets

By end of roadmap:

1. **TrueBalance** — flagship backend project. Fully featured, tested, containerized, deployed, with CI/CD
2. **Standalone backend project** — URL shortener / expense API / similar
3. **ML project(s)** — 2–3 Kaggle or personal projects
4. **RAG app** — deployed, demonstrates AI + backend integration
5. **Clean GitHub** — consistent commits, good READMEs, architecture diagrams
6. **Resume + LinkedIn** — ready for backend / AI backend roles

---

## 📅 Timeline Summary

| Months | Phase |
|--------|-------|
| 1 | Phase 1 — Python Foundations |
| 2–3 | Phase 2 — Database Mastery |
| 4–5 | Phase 3 — API Development |
| 6–7 | Phase 4 — Auth, Security & Async |
| 8–9 | Phase 5 — Quality & Containers |
| 10–11 | Phase 6 — Scaling & Infrastructure |
| 12–13 | Phase 7 — Architecture & Deployment |
| 14 | Phase 8 — Portfolio Finalization |
| 15–17 | Phase 9 — CS Core (Networks + OS) + DSA starts |
| 18–22 | Phase 10 — DSA continues (parallel) |
| 15–18 | Phase 11 — AI/ML Foundations |
| 19–21 | Phase 12 — Deep Learning |
| 22–23 | Phase 13 — RAG & LLM Engineering |
| 24–26 | Buffer — revision, interviews, catch-up |

> Phases 10–13 overlap intentionally. DSA is daily habit (30–45 min), not a full-time phase.


# 🗺️ Master Learning Roadmap — With Resources

**Total Timeline:** ~36 months | **Daily commitment:** 2–3 hrs/day
**Goal:** Backend Dev + CS Core + AI/ML/RAG — fully hireable backend + AI engineer

> 📌 Resources listed per topic. Free resources prioritized. Paid alternatives noted where free options are weak.

---

## Phase 1 — Python Foundations
**Duration: 1 month**

### Python Advanced

| Topic | Resource | Link | Free? |
|---|---|---|---|
| OOP (classes, inheritance, polymorphism, dunder) | Bro Code — Python OOP Full Course | https://www.youtube.com/watch?v=IbMDCwVm63M | ✅ |
| OOP (property decorators, getters/setters) | Corey Schafer — Property Decorators | https://youtu.be/jCzT9XFZ5bw | ✅ |
| Decorators | Corey Schafer — Decorators Playlist | https://www.youtube.com/watch?v=FsAPt_9Bf3U | ✅ |
| Generators | Corey Schafer — Generators | https://www.youtube.com/watch?v=bD05uGo_sVI | ✅ |
| Context Managers | Corey Schafer — Context Managers | https://www.youtube.com/watch?v=-aKFBoZpiqA | ✅ |
| Type hints | Corey Schafer — Python Tips & Tricks | https://www.youtube.com/watch?v=C-gEQdGVXbk | ✅ |
| Exception Handling (custom exceptions) | Corey Schafer — Try/Except Blocks | https://www.youtube.com/watch?v=NIWwJbo-9_8| ✅ |
| File I/O + JSON | Corey Schafer — File Objects | https://www.youtube.com/watch?v=Uh2ebFW8OYM | ✅ |
| Virtual Environments, pip, requirements.txt | Corey Schafer — VENV (Windows) | https://www.youtube.com/watch?v=APOPm01BVrk | ✅ |
| Environment Variables (.env) | Corey Schafer — Manage Multiple Projects & Env Variables | https://www.youtube.com/watch?v=5iWhQWVXosU | ✅ |
| Logging | Corey Schafer — Logging Basics | https://www.youtube.com/watch?v=-ARI4Cz-awo | ✅ |

### Git & Tooling

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Branching, merge, rebase, conflicts | Corey Schafer — Git Tutorial for Beginners | https://www.youtube.com/watch?v=HVsySz-h9r4 | ✅ |
| Clean commit history, PR workflow | Fireship — 13 Advanced Git Tips | https://www.youtube.com/watch?v=ecK3EnyGD8o | ✅ |

### ✅ Milestone
- Strong Python fundamentals beyond basics
- Clean, professional coding habits in place

---

## Phase 2 — Database Mastery
**Duration: 2 months**

### SQL Querying

| Topic | Resource | Link | Free? |
|---|---|---|---|
| All JOINs, GROUP BY, HAVING, subqueries | CodeWithHarry — SQL Full Course (Hindi) | https://www.youtube.com/watch?v=hlGoQC332VM | ✅ |
| Window Functions, CTEs | TechTFQ — Window Functions Series | https://www.youtube.com/watch?v=Ww71knvhQ-s | ✅ |
| Advanced SQL Practice | DataLemur — Free SQL Questions | https://datalemur.com | ✅ |

### Schema Design & Normalization

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Normalization (1NF-3NF), schema design | Decomplexify — Database Normalization | https://www.youtube.com/watch?v=GFQaEYEc8_8 | ✅ |
| Foreign keys and constraints | Practical SQL — documentation + exercises | https://docs.postgresql.org | ✅ |

### Indexing & Query Optimization

| Topic | Resource | Link | Free? |
|---|---|---|---|
| B-tree internals, indexing concepts, EXPLAIN ANALYZE | Hussein Nasser — Postgres Indexing | https://www.youtube.com/watch?v=fsG1XaZEa78 | ✅ |

### Transactions & ACID

| Topic | Resource | Link | Free? |
|---|---|---|---|
| ACID, isolation levels, deadlocks | Hussein Nasser — Database Transactions | https://www.youtube.com/watch?v=pomxJOFVcQs | ✅ |

### ORM (SQLAlchemy + Alembic)

| Topic | Resource | Link | Free? |
|---|---|---|---|
| SQLAlchemy models, relationships, querying | ArjanCodes — SQLAlchemy Tutorial | https://www.youtube.com/watch?v=398-uAIL5cM | ✅ |
| Alembic migrations | YouTube — FastAPI PostgreSQL + Alembic (Part 15) | https://www.youtube.com/watch?v=e8NnDz8uT7o | ✅ |

### ✅ Milestone
- Comfortable designing schemas from scratch
- Can read and optimize query plans
- ORM-based data layer working in TrueBalance

---

## Phase 3 — API Development
**Duration: 2 months**

### FastAPI (all topics)

| Topic | Resource | Link | Free? |
|---|---|---|---|
| FastAPI full course (routing, Pydantic, DI, middleware, auth, deployment) | Amigoscode — FastAPI Full Tutorial | https://www.youtube.com/watch?v=tLKKmouUams | ✅ |
| FastAPI Beyond CRUD (advanced patterns, auth, testing) | FastAPI Beyond CRUD — Full Course | https://www.youtube.com/watch?v=TO4aQ3ghFOc | ✅ |
| Official FastAPI docs (reference alongside videos) | FastAPI Official Docs | https://fastapi.tiangolo.com | ✅ |

### REST API Design Principles

| Topic | Resource | Link | Free? |
|---|---|---|---|
| REST conventions, status codes, idempotency, pagination | Hussein Nasser — REST API Design Best Practices | https://www.youtube.com/watch?v=_YlYuNMTCc8 | ✅ |

### ✅ Milestone
- Can design a clean, well-documented REST API from scratch
- TrueBalance API follows REST best practices

---

## Phase 4 — Auth, Security & Async
**Duration: 2 months**
> ⚠️ Dense phase. Reduce to 1.5 hrs/day if needed. DSA takes priority here.

### Authentication & Authorization

| Topic | Resource | Link | Free? |
|---|---|---|---|
| JWT, bcrypt, OAuth2, RBAC in FastAPI | Covered inside FastAPI Beyond CRUD (Phase 3 video) | https://www.youtube.com/watch?v=TO4aQ3ghFOc | ✅ |
| JWT deep dive | Fireship — JWT Explained in 100 Seconds | https://www.youtube.com/watch?v=UBUNrFtufWo | ✅ |

### Security

| Topic | Resource | Link | Free? |
|---|---|---|---|
| OWASP Top 10 | Web Dev Simplified — OWASP Top 10 | https://www.youtube.com/watch?v=jYL77rE-M6Y | ✅ |

### Async Programming

| Topic | Resource | Link | Free? |
|---|---|---|---|
| asyncio, event loop, async/await deeply | ArjanCodes — asyncio in Python | https://www.youtube.com/watch?v=2IW-ZEui4h4 | ✅ |
| Async in FastAPI (asyncpg, when to use) | Covered inside FastAPI Beyond CRUD above | https://www.youtube.com/watch?v=TO4aQ3ghFOc | ✅ |

### ✅ Milestone
- Secure, role-protected API
- Understand async tradeoffs, not just syntax

---

## Phase 5 — Quality & Containers
**Duration: 2 months**

### Testing

| Topic | Resource | Link | Free? |
|---|---|---|---|
| pytest fundamentals (fixtures, parametrize, mocking) | freeCodeCamp — Pytest Full Course | https://www.youtube.com/watch?v=cHYq1MRoyI0 | ✅ |
| Integration testing with FastAPI TestClient | Covered inside FastAPI Beyond CRUD above | https://www.youtube.com/watch?v=TO4aQ3ghFOc | ✅ |

### Docker

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Docker full course (images, containers, Dockerfile, volumes, networking) | TechWorldWithNana — Docker for Beginners | https://www.youtube.com/watch?v=3c-iBn73dDE | ✅ |
| docker-compose for multi-container setups | Included in same TechWorldWithNana video above | https://www.youtube.com/watch?v=3c-iBn73dDE | ✅ |

### ✅ Milestone
- 70%+ test coverage on TrueBalance
- TrueBalance runs anywhere via docker-compose

---

## Phase 6 — Scaling & Infrastructure
**Duration: 2 months**

### Redis & Caching

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Redis fundamentals + caching in Python | Master Redis with Python — Crash Course | https://www.youtube.com/watch?v=xDUDVpxLkok | ✅ |
| Redis data types + cache-aside pattern | Redis in Python (2024) | https://www.youtube.com/watch?v=-Q9rSBMKSkE | ✅ |

### Message Queues (Celery)

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Celery + Redis + FastAPI full guide | TestDriven.io — Celery + FastAPI (Definitive Guide) | https://testdriven.io/courses/fastapi-celery/ | 💰 Paid |
| Celery intro (free alternative) | Pretty Printed — Celery with Flask | https://www.youtube.com/watch?v=iwxzilyxTDM | ✅ |

### Linux / CLI

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Linux CLI full course (permissions, SSH, processes, bash) | freeCodeCamp — Linux CLI Full Course | https://www.youtube.com/watch?v=sWbUDq4S6Y8 | ✅ |
| grep/sed/awk for log parsing | Corey Schafer — Linux Terminal Commands | https://www.youtube.com/watch?v=ZtqBQ68cfJc | ✅ |

### Git Deepening

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Merge vs rebase, branching, conflict resolution | Atlassian Git tutorials (docs, free) | https://www.atlassian.com/git/tutorials | ✅ |

### ✅ Milestone
- Measurable performance improvement via caching
- Comfortable with Linux server environment

---

## Phase 7 — Architecture & Deployment
**Duration: 2 months**

### System Design

| Topic | Resource | Link | Free? |
|---|---|---|---|
| System design fundamentals (client-server, scaling, load balancing, caching in systems) | ByteByteGo — System Design YouTube | https://www.youtube.com/@ByteByteGo | ✅ |
| System design interview prep (case studies) | Gaurav Sen — System Design Playlist | https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX | ✅ |

### Deployment & CI/CD

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Deploy FastAPI to Render/Railway | Render official docs | https://render.com/docs | ✅ |
| AWS EC2 basics | freeCodeCamp — AWS Cloud Practitioner Full Course | https://www.youtube.com/watch?v=SOTamWNgDKc | ✅ |
| GitHub Actions CI/CD pipeline | TechWorldWithNana — GitHub Actions Full Course | https://www.youtube.com/watch?v=R8_veQiYBjI | ✅ |

### ✅ Milestone
- Can explain system design tradeoffs out loud
- TrueBalance is live and auto-deploying

---

## Phase 8 — Portfolio Finalization
**Duration: 1 month**

> No specific course needed here. This is pure building + polishing.

- Build URL shortener / second standalone project
- README, architecture diagram, LinkedIn/resume polish
- Mock interviews: practice explaining TrueBalance end-to-end

### ✅ Milestone
- Portfolio recruiter-ready
- Can defend every design decision confidently

---

## Phase 9 — CS Core: Networks & OS
**Duration: 3 months**

### Computer Networks

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Full computer networking course (OSI, TCP/IP, HTTP, DNS, TLS, sockets) | freeCodeCamp — Computer Networking Full Course | https://www.youtube.com/watch?v=qiQR5rTSshw | ✅ |
| HTTP deep dive | Hussein Nasser — HTTP Crash Course | https://www.youtube.com/watch?v=0OrmKCB0UrQ | ✅ |
| TLS/SSL explained | Hussein Nasser — TLS/HTTPS Explained | https://www.youtube.com/watch?v=j9QmMEWmcfo | ✅ |

### Operating Systems

| Topic | Resource | Link | Free? |
|---|---|---|---|
| OS concepts (processes, threads, concurrency, memory) | freeCodeCamp — Operating Systems Full Course | https://www.youtube.com/watch?v=yK1uBHPdp30 | ✅ |
| Book (free online, selective chapters) | Operating Systems: Three Easy Pieces | https://pages.cs.wisc.edu/~remzi/OSTEP/ | ✅ |

### ✅ Milestone
- Can answer CN + OS interview questions confidently
- Understand how HTTP, TCP, and processes work under the hood

---

## Phase 10 — DSA: Post-Recursion (Striver Sheet)
**Duration: 5 months (parallel with Phases 9–12)**
> 💡 30–45 min daily alongside main phase. Full focus on weekends.

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Full Striver A2Z DSA Sheet (C++) | TakeUForward — A2Z DSA Course | https://www.youtube.com/@takeUforward | ✅ |
| Abdul Bari — conceptual depth on algorithms | Abdul Bari — Algorithms | https://www.youtube.com/watch?v=0IAPZzGSbME | ✅ |
| Practice platform | LeetCode | https://leetcode.com | ✅ |

### ✅ Milestone
- Can solve medium LeetCode problems independently
- Recognizes patterns, not just solutions

---

## Phase 11 — AI/ML Foundations
**Duration: 4 months**

### Math Refresh

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Linear algebra, probability, calculus (intuition) | 3Blue1Brown — Essence of Linear Algebra | https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab | ✅ |
| Statistics & probability for ML | StatQuest with Josh Starmer | https://www.youtube.com/@statquest | ✅ |

### Core ML

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Full ML course (regression, classification, trees, evaluation, overfitting) | Andrew Ng — Machine Learning Specialization (Coursera) | https://www.coursera.org/specializations/machine-learning-introduction | ✅ Audit free |
| Practical ML with scikit-learn | Kaggle Learn — ML Courses | https://www.kaggle.com/learn | ✅ |

### Practice

| Topic | Resource | Link | Free? |
|---|---|---|---|
| End-to-end ML projects | Kaggle Competitions | https://www.kaggle.com/competitions | ✅ |

### ✅ Milestone
- Can build, train, evaluate ML models from scratch
- 2–3 ML projects on GitHub

---

## Phase 12 — Deep Learning
**Duration: 3 months**

| Topic | Resource | Link | Free? |
|---|---|---|---|
| Neural networks fundamentals + backpropagation (build from scratch) | Andrej Karpathy — Neural Networks: Zero to Hero | https://www.youtube.com/playlist?list=PLXYLzZ3XzIbi4lL43O6fIU_ojuZwBO6vi | ✅ |
| Deep learning theory (CNNs, RNNs, transformers, optimizers) | Andrew Ng — Deep Learning Specialization (Coursera) | https://www.coursera.org/specializations/deep-learning | ✅ Audit free |
| PyTorch practical implementation | freeCodeCamp — PyTorch Full Course | https://www.youtube.com/watch?v=V_xro1bcAuA | ✅ |
| HuggingFace fine-tuning | HuggingFace Course (free, official) | https://huggingface.co/learn/nlp-course | ✅ |

### ✅ Milestone
- Understand transformer architecture deeply
- Can fine-tune HuggingFace models
- At least 1 DL project deployed

---

## Phase 13 — RAG & LLM Engineering
**Duration: 2 months**

| Topic | Resource | Link | Free? |
|---|---|---|---|
| LLM fundamentals, prompt engineering, APIs | DeepLearning.AI Short Courses (free) — ChatGPT Prompt Engineering | https://www.deeplearning.ai/short-courses/ | ✅ |
| RAG from scratch (embeddings, vector DBs, chunking, retrieval pipeline) | freeCodeCamp — RAG from Scratch (LangChain engineer) | https://www.youtube.com/watch?v=sVcwVQRHIc8 | ✅ |
| LangChain / LlamaIndex full course | Activeloop — RAG with LlamaIndex + LangChain | https://learn.activeloop.ai/courses/rag | ✅ |
| Vector databases (Pinecone, Chroma) | Pinecone Learning Center | https://www.pinecone.io/learn/ | ✅ |
| Integrating RAG into FastAPI (production) | Build from TrueBalance foundation — no specific course, apply Phase 3+13 knowledge | — | — |

### ✅ Milestone
- Can design and deploy a production RAG system
- Backend + AI skills merge — full-stack AI backend engineer profile

---

## 📅 Timeline Summary

| Months | Phase |
|---|---|
| Month 1 | Phase 1 — Python Foundations |
| Months 2–3 | Phase 2 — Database Mastery |
| Months 4–5 | Phase 3 — API Development |
| Months 6–7 | Phase 4 — Auth, Security & Async |
| Months 8–9 | Phase 5 — Quality & Containers |
| Months 10–11 | Phase 6 — Scaling & Infrastructure |
| Months 12–13 | Phase 7 — Architecture & Deployment |
| Month 14 | Phase 8 — Portfolio Finalization |
| Months 15–17 | Phase 9 — CS Core (Networks + OS) |
| Months 15–22 | Phase 10 — DSA (parallel, 30–45 min/day) |
| Months 15–18 | Phase 11 — AI/ML Foundations |
| Months 19–21 | Phase 12 — Deep Learning |
| Months 22–23 | Phase 13 — RAG & LLM Engineering |
| Months 24–26 | Buffer — revision, catch-up, interview prep |

> Phases 10–13 overlap intentionally. DSA is daily habit (30–45 min), not a full-time phase.

---

## 🔑 Resource Legend

| Symbol | Meaning |
|---|---|
| ✅ | Free |
| 💰 Paid | Paid course (Udemy/Coursera/TestDriven.io) |
| ✅ Audit free | Free to audit, paid for certificate |


