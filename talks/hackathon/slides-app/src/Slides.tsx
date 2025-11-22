import React, { useEffect, useRef } from 'react';
import Reveal from 'reveal.js';
import 'reveal.js/dist/reveal.css';
import 'reveal.js/dist/theme/black.css';
import { slidesContent } from './slides-content';

const Slides: React.FC = () => {
  const deckDivRef = useRef<HTMLDivElement>(null);
  const deckRef = useRef<Reveal.Api | null>(null);

  useEffect(() => {
    if (deckRef.current) return;

    deckRef.current = new Reveal(deckDivRef.current!, {
      hash: true,
      controls: true,
      progress: true,
      center: true,
      transition: 'slide',
      backgroundTransition: 'fade',
    });

    deckRef.current.initialize();

    return () => {
      try {
        if (deckRef.current) {
          deckRef.current.destroy();
          deckRef.current = null;
        }
      } catch (e) {
        console.warn('Reveal destroy error:', e);
      }
    };
  }, []);

  return (
    <div className="reveal" ref={deckDivRef} style={{ height: '100vh' }}>
      <div
        className="slides"
        dangerouslySetInnerHTML={{ __html: slidesContent }}
        style={{
          color: '#eaeaea',
          fontFamily: "'Segoe UI', Arial, sans-serif"
        }}
      />
      <style>{`
        .reveal {
          background-color: #1a1a2e;
        }
        .reveal .slides {
          text-align: left;
        }
        .reveal h1,
        .reveal h2,
        .reveal h3 {
          color: #00d4ff;
          font-weight: normal;
          text-transform: none;
        }
        .reveal h1 {
          font-size: 2.2em;
        }
        .reveal h2 {
          font-size: 1.5em;
        }
        .reveal strong {
          color: #ff6b6b;
        }
        .reveal code,
        .reveal pre {
          background: #16213e;
          color: #00d4ff;
          padding: 5px 10px;
          border-radius: 4px;
        }
        .reveal pre {
          box-shadow: none;
          width: 100%;
          font-size: 0.8em;
        }
        .reveal a {
          color: #4ecdc4;
        }
        .reveal blockquote {
          border-left: 4px solid #00d4ff;
          background: #16213e;
          padding: 20px;
          font-style: italic;
          color: #eaeaea;
          margin: 20px 0;
        }
        .reveal ul,
        .reveal ol {
          display: block;
          margin-left: 1em;
        }
        .reveal .slides section {
          height: 100%;
        }
        .reveal table {
          margin: 20px 0;
          border-collapse: collapse;
        }
        .reveal th,
        .reveal td {
          border: 1px solid #2a3f5f !important;
          padding: 10px !important;
        }
        .reveal th {
          background: #0f1527 !important;
          color: #00d4ff !important;
          font-weight: bold;
        }
        .reveal td {
          background: #1a2332 !important;
          color: #eaeaea !important;
        }
        .reveal tr:nth-child(even) td {
          background: #16213e !important;
        }
        .reveal .progress {
          color: #00d4ff;
        }
        .reveal .controls {
          color: #00d4ff;
        }
      `}</style>
    </div>
  );
};

export default Slides;