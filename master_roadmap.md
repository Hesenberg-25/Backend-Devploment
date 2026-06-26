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
