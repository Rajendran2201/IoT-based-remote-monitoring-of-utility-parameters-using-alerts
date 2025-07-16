// src/components/ui/Button.tsx
import React from 'react';

type ButtonProps = {
  children: React.ReactNode;
  className?: string;
};

export function Button({ children, className = '' }: ButtonProps) {
  return (
    <button
      className={`bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-xl transition ${className}`}
    >
      {children}
    </button>
  );
}
