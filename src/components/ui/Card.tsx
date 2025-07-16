// src/components/ui/Card.tsx
import React from 'react';

type CardProps = React.HTMLAttributes<HTMLDivElement> & {
  children: React.ReactNode;
};

export function Card({ children, className = '', ...props }: CardProps) {
  return (
    <div
      className={`bg-white rounded-2xl shadow-md p-4 transition-all ${className}`}
      {...props}
    >
      {children}
    </div>
  );
}

type CardContentProps = React.HTMLAttributes<HTMLDivElement> & {
  children: React.ReactNode;
};

export function CardContent({ children, className = '', ...props }: CardContentProps) {
  return (
    <div className={`text-gray-800 ${className}`} {...props}>
      {children}
    </div>
  );
}
