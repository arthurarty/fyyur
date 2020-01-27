--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Artist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Artist" (
    id integer NOT NULL,
    name character varying,
    phone character varying(120),
    image_link character varying(500),
    facebook_link character varying(120),
    seeking_description character varying(500),
    seeking_venue boolean,
    website character varying(250),
    city_id integer NOT NULL
);


ALTER TABLE public."Artist" OWNER TO postgres;

--
-- Name: Artist_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Artist_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Artist_id_seq" OWNER TO postgres;

--
-- Name: Artist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Artist_id_seq" OWNED BY public."Artist".id;


--
-- Name: City; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."City" (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    state_id integer NOT NULL
);


ALTER TABLE public."City" OWNER TO postgres;

--
-- Name: City_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."City_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."City_id_seq" OWNER TO postgres;

--
-- Name: City_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."City_id_seq" OWNED BY public."City".id;


--
-- Name: Genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Genre" (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public."Genre" OWNER TO postgres;

--
-- Name: Genre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Genre_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Genre_id_seq" OWNER TO postgres;

--
-- Name: Genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Genre_id_seq" OWNED BY public."Genre".id;


--
-- Name: Show; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Show" (
    id integer NOT NULL,
    artist_id integer NOT NULL,
    venue_id integer NOT NULL,
    start_time timestamp without time zone NOT NULL
);


ALTER TABLE public."Show" OWNER TO postgres;

--
-- Name: Show_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Show_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Show_id_seq" OWNER TO postgres;

--
-- Name: Show_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Show_id_seq" OWNED BY public."Show".id;


--
-- Name: State; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."State" (
    id integer NOT NULL,
    name character varying(2) NOT NULL
);


ALTER TABLE public."State" OWNER TO postgres;

--
-- Name: State_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."State_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."State_id_seq" OWNER TO postgres;

--
-- Name: State_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."State_id_seq" OWNED BY public."State".id;


--
-- Name: Venue; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Venue" (
    id integer NOT NULL,
    name character varying,
    address character varying(120),
    phone character varying(120),
    image_link character varying(500),
    facebook_link character varying(120),
    seeking_description character varying(500),
    seeking_talent boolean,
    website character varying(250),
    city_id integer NOT NULL
);


ALTER TABLE public."Venue" OWNER TO postgres;

--
-- Name: Venue_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Venue_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Venue_id_seq" OWNER TO postgres;

--
-- Name: Venue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Venue_id_seq" OWNED BY public."Venue".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: genres_artists; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genres_artists (
    artist_id integer NOT NULL,
    genre_id integer NOT NULL
);


ALTER TABLE public.genres_artists OWNER TO postgres;

--
-- Name: genres_venues; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genres_venues (
    venue_id integer NOT NULL,
    genre_id integer NOT NULL
);


ALTER TABLE public.genres_venues OWNER TO postgres;

--
-- Name: Artist id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artist" ALTER COLUMN id SET DEFAULT nextval('public."Artist_id_seq"'::regclass);


--
-- Name: City id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."City" ALTER COLUMN id SET DEFAULT nextval('public."City_id_seq"'::regclass);


--
-- Name: Genre id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Genre" ALTER COLUMN id SET DEFAULT nextval('public."Genre_id_seq"'::regclass);


--
-- Name: Show id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Show" ALTER COLUMN id SET DEFAULT nextval('public."Show_id_seq"'::regclass);


--
-- Name: State id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."State" ALTER COLUMN id SET DEFAULT nextval('public."State_id_seq"'::regclass);


--
-- Name: Venue id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Venue" ALTER COLUMN id SET DEFAULT nextval('public."Venue_id_seq"'::regclass);


--
-- Data for Name: Artist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Artist" (id, name, phone, image_link, facebook_link, seeking_description, seeking_venue, website, city_id) FROM stdin;
1	Matt Quevedo	2063769840	https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80	http://facebook.com	We are on the lookout for a local artist to play every two weeks. Please call us.	t	https://www.parksquarelivemusicandcoffee.com	1
2	Guns N Petals	326-123-5000	https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80	https://www.facebook.com/GunsNPetals	Looking for shows to perform at in the San Francisco Bay Area!	t	https://www.gunsnpetalsband.com	1
\.


--
-- Data for Name: City; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."City" (id, name, state_id) FROM stdin;
1	San Francisco	5
2	New York	27
\.


--
-- Data for Name: Genre; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Genre" (id, name) FROM stdin;
1	Alternative
2	Blues
3	Classical
4	Country
5	Electronic
6	Folk
7	Funk
8	Hip-Hop
9	Heavy Metal
10	Instrumental
11	Jazz
12	Musical Theatre
13	Pop
14	Punk
15	R&B
16	Reggae
17	Rock n Roll
18	Soul
19	Other
\.


--
-- Data for Name: Show; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Show" (id, artist_id, venue_id, start_time) FROM stdin;
1	1	1	2020-10-27 19:29:35
2	1	2	2020-09-27 19:29:35
3	2	1	2020-04-27 19:29:35
\.


--
-- Data for Name: State; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."State" (id, name) FROM stdin;
1	AL
2	AK
3	AZ
4	AR
5	CA
6	CO
7	CT
8	DE
9	DC
10	FL
11	GA
12	HI
13	ID
14	IL
15	IN
16	IA
17	KS
18	KY
19	LA
20	ME
21	MT
22	NE
23	NV
24	NH
25	NJ
26	NM
27	NY
28	NC
29	ND
30	OH
31	OK
32	OR
33	MD
34	MA
35	MI
36	MN
37	MS
38	MO
39	PA
40	RI
41	SC
42	SD
43	TN
44	TX
45	UT
46	VT
47	VA
48	WA
49	WV
50	WI
51	WY
\.


--
-- Data for Name: Venue; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Venue" (id, name, address, phone, image_link, facebook_link, seeking_description, seeking_talent, website, city_id) FROM stdin;
1	The Musical Hop	1015 Folsom Street	123-123-1234	https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60	https://www.facebook.com/TheMusicalHop	We are on the lookout for a local artist to play every two weeks. Please call us.	t	https://www.themusicalhop.com	1
2	The Dueling Pianos Bar	335 Delancey Street	914-003-1132	https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80	https://www.facebook.com/theduelingpianos		f	https://www.theduelingpianos.com	2
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
ec68b3e27615
\.


--
-- Data for Name: genres_artists; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.genres_artists (artist_id, genre_id) FROM stdin;
1	4
2	17
\.


--
-- Data for Name: genres_venues; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.genres_venues (venue_id, genre_id) FROM stdin;
1	2
1	3
1	8
1	9
2	3
2	8
2	15
\.


--
-- Name: Artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Artist_id_seq"', 2, true);


--
-- Name: City_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."City_id_seq"', 2, true);


--
-- Name: Genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Genre_id_seq"', 19, true);


--
-- Name: Show_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Show_id_seq"', 3, true);


--
-- Name: State_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."State_id_seq"', 51, true);


--
-- Name: Venue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Venue_id_seq"', 2, true);


--
-- Name: Artist Artist_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artist"
    ADD CONSTRAINT "Artist_name_key" UNIQUE (name);


--
-- Name: Artist Artist_phone_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artist"
    ADD CONSTRAINT "Artist_phone_key" UNIQUE (phone);


--
-- Name: Artist Artist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artist"
    ADD CONSTRAINT "Artist_pkey" PRIMARY KEY (id);


--
-- Name: City City_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."City"
    ADD CONSTRAINT "City_name_key" UNIQUE (name);


--
-- Name: City City_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."City"
    ADD CONSTRAINT "City_pkey" PRIMARY KEY (id);


--
-- Name: Genre Genre_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Genre"
    ADD CONSTRAINT "Genre_name_key" UNIQUE (name);


--
-- Name: Genre Genre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Genre"
    ADD CONSTRAINT "Genre_pkey" PRIMARY KEY (id);


--
-- Name: Show Show_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Show"
    ADD CONSTRAINT "Show_pkey" PRIMARY KEY (id);


--
-- Name: State State_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."State"
    ADD CONSTRAINT "State_name_key" UNIQUE (name);


--
-- Name: State State_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."State"
    ADD CONSTRAINT "State_pkey" PRIMARY KEY (id);


--
-- Name: Venue Venue_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Venue"
    ADD CONSTRAINT "Venue_pkey" PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: genres_artists genres_artists_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_artists
    ADD CONSTRAINT genres_artists_pkey PRIMARY KEY (artist_id, genre_id);


--
-- Name: genres_venues genres_venues_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_venues
    ADD CONSTRAINT genres_venues_pkey PRIMARY KEY (venue_id, genre_id);


--
-- Name: Show unique_show; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Show"
    ADD CONSTRAINT unique_show UNIQUE (artist_id, venue_id, start_time);


--
-- Name: Venue unique_venue; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Venue"
    ADD CONSTRAINT unique_venue UNIQUE (name, address, city_id);


--
-- Name: Artist Artist_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artist"
    ADD CONSTRAINT "Artist_city_id_fkey" FOREIGN KEY (city_id) REFERENCES public."City"(id);


--
-- Name: City City_state_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."City"
    ADD CONSTRAINT "City_state_id_fkey" FOREIGN KEY (state_id) REFERENCES public."State"(id);


--
-- Name: Show Show_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Show"
    ADD CONSTRAINT "Show_artist_id_fkey" FOREIGN KEY (artist_id) REFERENCES public."Artist"(id);


--
-- Name: Show Show_venue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Show"
    ADD CONSTRAINT "Show_venue_id_fkey" FOREIGN KEY (venue_id) REFERENCES public."Venue"(id);


--
-- Name: Venue Venue_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Venue"
    ADD CONSTRAINT "Venue_city_id_fkey" FOREIGN KEY (city_id) REFERENCES public."City"(id);


--
-- Name: genres_artists genres_artists_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_artists
    ADD CONSTRAINT genres_artists_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES public."Artist"(id);


--
-- Name: genres_artists genres_artists_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_artists
    ADD CONSTRAINT genres_artists_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public."Genre"(id);


--
-- Name: genres_venues genres_venues_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_venues
    ADD CONSTRAINT genres_venues_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public."Genre"(id);


--
-- Name: genres_venues genres_venues_venue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_venues
    ADD CONSTRAINT genres_venues_venue_id_fkey FOREIGN KEY (venue_id) REFERENCES public."Venue"(id);


--
-- PostgreSQL database dump complete
--

